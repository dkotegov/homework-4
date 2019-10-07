# -*- coding: utf-8 -*-

import time
import unittest

from selenium import webdriver

from page import AuthPage


def get_auth_form():
    auth_page = AuthPage(webdriver.Firefox())
    auth_page.switch_to_login_iframe()
    return auth_page


class TestMethods(unittest.TestCase):
    def test_correct_auth(self):
        auth_page = get_auth_form()
        auth_page.enter_email('opg_plus')
        auth_page.submit()
        auth_page.enter_password('MoreThenTests')
        auth_page.submit()

        auth_page.wait_redirect("https://e.mail.ru/messages/inbox\?.*")
        auth_page.quit()

    def test_yandex_auth(self):
        auth_page = get_auth_form()
        auth_page.select_yandex_provider()
        auth_page.enter_email('example')
        auth_page.submit()

        auth_page.wait_redirect("https://passport.yandex.ru.*")
        auth_page.quit()

    def test_google_auth(self):
        auth_page = get_auth_form()
        auth_page.select_google_provider()
        auth_page.enter_email('example')
        auth_page.submit()

        auth_page.wait_redirect("https://accounts.google.com.*")
        auth_page.quit()

    def test_yahoo_auth(self):
        auth_page = get_auth_form()
        auth_page.select_yahoo_provider()
        auth_page.enter_email('example')
        auth_page.submit()

        auth_page.wait_redirect("https://login.yahoo.com.*")
        auth_page.quit()

    def test_other_auth(self):
        auth_page = get_auth_form()
        auth_page.select_other_provider()
        auth_page.enter_email('example@example.com')
        auth_page.submit()

        auth_page.wait_password_field()
        auth_page.quit()

    def test_remind_click(self):
        auth_page = get_auth_form()
        auth_page.click_remind_password()

        auth_page.wait_redirect("https://account.mail.ru/recovery\?.*")
        auth_page.quit()

    def test_remind_click_2(self):
        auth_page = get_auth_form()
        auth_page.enter_email('opg_plus')
        auth_page.submit()
        auth_page.wait_password_field()
        auth_page.click_remind_password()

        auth_page.wait_redirect("https://account.mail.ru/recovery\?.*")
        auth_page.quit()

    def test_signup_click(self):
        auth_page = get_auth_form()
        auth_page.click_signup()

        auth_page.wait_redirect("https://account.mail.ru/signup\?.*")
        auth_page.quit()

    def test_correct_email(self):
        auth_page = get_auth_form()
        auth_page.enter_email('opg_plus')
        auth_page.submit()

        auth_page.wait_password_field()
        auth_page.quit()

    def test_empty_email(self):
        auth_page = get_auth_form()
        auth_page.submit()

        error = auth_page.get_email_error()
        self.assertNotEqual(error, '')
        auth_page.quit()

    def test_incorrect_email(self):
        auth_page = get_auth_form()
        auth_page.enter_email('this_is_incorrect_email_for_testing_email_input')
        auth_page.submit()

        error = auth_page.get_email_error()
        self.assertNotEqual(error, '')
        auth_page.quit()

    def test_cyrillic_email(self):
        auth_page = get_auth_form()
        auth_page.enter_email('русский')
        auth_page.submit()

        error = auth_page.get_email_error()
        self.assertNotEqual(error, '')
        auth_page.quit()

    def test_empty_password(self):
        auth_page = get_auth_form()
        auth_page.enter_email('opg_plus')
        auth_page.submit()
        auth_page.wait_password_field()
        auth_page.submit()

        error = auth_page.get_email_error()
        self.assertNotEqual(error, '')
        auth_page.quit()

    def test_incorrect_password(self):
        auth_page = get_auth_form()
        auth_page.enter_email('opg_plus')
        auth_page.submit()
        auth_page.enter_password('IncorrectPassword!')
        auth_page.submit()

        auth_page.wait_redirect("https://account.mail.ru/login\?.*")
        auth_page.quit()

    def test_other_domain_email(self):
        auth_page = get_auth_form()
        auth_page.enter_email('example@example.com')

        self.assertIsNone(auth_page.get_domain_list())
        auth_page.quit()

    def test_default_domain_after_other_domain_select(self):
        auth_page = get_auth_form()
        auth_page.select_yandex_provider()
        auth_page.enter_email('example@example.com')
        auth_page.clear_email()

        self.assertEqual(auth_page.get_domain(), "@yandex.ru")
        auth_page.quit()

    def test_yandex_provider_select(self):
        auth_page = get_auth_form()
        auth_page.select_yandex_provider()

        self.assertEqual(auth_page.get_domain(), "@yandex.ru")
        auth_page.quit()

    def test_google_provider_select(self):
        auth_page = get_auth_form()
        auth_page.select_google_provider()

        self.assertEqual(auth_page.get_domain(), "@gmail.com")
        auth_page.quit()

    def test_yahoo_provider_select(self):
        auth_page = get_auth_form()
        auth_page.select_yahoo_provider()

        self.assertEqual(auth_page.get_domain(), "@yahoo.com")
        auth_page.quit()
