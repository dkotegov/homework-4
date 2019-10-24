# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.page_auth import AuthPage


class TestAuth(unittest.TestCase):
    EMAIL = os.getenv('EMAIL', 'opg_plus')
    PASSWORD = os.getenv("PASSWORD")

    def setUp(self):
        if self.PASSWORD is None:
            raise ValueError("Password env-var is None")
        browser = os.getenv("SELENIUM_TEST_BROWSER", "CHROME")
        self.driver = Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.form = AuthPage(self.driver)
        self.form.switch_to_login_iframe()

    def tearDown(self):
        self.driver.quit()

    def test_correct_auth(self):
        self.form.enter_email(self.EMAIL)
        self.form.submit()
        self.form.enter_password(self.PASSWORD)
        self.form.submit()

        self.form.wait_redirect("https://e.mail.ru/messages/inbox\?.*")

    def test_yandex_auth(self):
        self.form.select_yandex_provider()
        self.form.enter_email('example')
        self.form.submit()

        self.form.wait_redirect("https://passport.yandex.ru.*")

    def test_google_auth(self):
        self.form.select_google_provider()
        self.form.enter_email('example')
        self.form.submit()

        self.form.wait_redirect("https://accounts.google.com.*")

    def test_yahoo_auth(self):
        self.form.select_yahoo_provider()
        self.form.enter_email('example')
        self.form.submit()

        self.form.wait_redirect("https://login.yahoo.com.*")

    def test_other_auth(self):
        self.form.select_other_provider()
        self.form.enter_email('example@example.com')
        self.form.submit()

        self.form.wait_password_visibility()

    def test_remind_click(self):
        self.form.click_remind_password()

        self.form.wait_redirect("https://account.mail.ru/recovery\?.*")

    def test_remind_click_2(self):
        self.form.enter_email(self.EMAIL)
        self.form.submit()
        self.form.wait_password_visibility()
        self.form.click_remind_password()

        self.form.wait_redirect("https://account.mail.ru/recovery\?.*")

    def test_signup_click(self):
        self.form.click_signup()

        self.form.wait_redirect("https://account.mail.ru/signup\?.*")

    def test_correct_email(self):
        self.form.enter_email(self.EMAIL)
        self.form.submit()

        self.form.wait_password_visibility()

    def test_empty_email(self):
        self.form.submit()

        error = self.form.get_email_error()
        self.assertEqual(error, 'Поле «Имя аккаунта» должно быть заполнено')

    def test_incorrect_email(self):
        self.form.enter_email('this_is_incorrect_email_for_testing_email_input')
        self.form.submit()

        error = self.form.get_email_error()
        self.assertEqual(error, 'Такой аккаунт не зарегистрирован')

    def test_cyrillic_email(self):
        self.form.enter_email('русский')
        self.form.submit()

        error = self.form.get_email_error()
        self.assertEqual(error, 'Такой аккаунт не зарегистрирован')

    def test_empty_password(self):
        self.form.enter_email(self.EMAIL)
        self.form.submit()
        self.form.wait_password_visibility()
        self.form.submit()

        error = self.form.get_email_error()
        self.assertEqual(error, 'Поле «Пароль» должно быть заполнено')

    def test_incorrect_password(self):
        self.form.enter_email(self.EMAIL)
        self.form.submit()
        self.form.enter_password('IncorrectPassword!')
        self.form.submit()

        self.form.wait_redirect("https://account.mail.ru/login\?.*")

    def test_other_domain_email(self):
        self.form.enter_email('example@example.com')

        self.assertIsNone(self.form.get_domain_list())

    def test_default_domain_after_other_domain_select(self):
        self.form.select_yandex_provider()
        self.form.enter_email('example@example.com')
        self.form.clear_email()

        self.assertEqual(self.form.get_domain(), "@yandex.ru")

    def test_yandex_provider_select(self):
        self.form.select_yandex_provider()

        self.assertEqual(self.form.get_domain(), "@yandex.ru")

    def test_google_provider_select(self):
        self.form.select_google_provider()

        self.assertEqual(self.form.get_domain(), "@gmail.com")

    def test_yahoo_provider_select(self):
        self.form.select_yahoo_provider()

        self.assertEqual(self.form.get_domain(), "@yahoo.com")
