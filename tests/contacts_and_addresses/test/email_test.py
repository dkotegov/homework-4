import os
import time
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from tests.contacts_and_addresses.src.auth_page import AuthPage
from tests.contacts_and_addresses.src.email_page import EmailPage


class EmailTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        # browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_error_ru(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        auth_page.top_menu.get_username()

        email_page = EmailPage(self.driver)
        email_page.open()

        email_form = email_page.form
        test_email = 'ваукакойты'
        email_form.add_email(test_email)
        error = email_form.check_error()
        self.assert_(error == 'Incorrect email address. Enter a different one.')

    def test_success_input(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        auth_page.top_menu.get_username()

        email_page = EmailPage(self.driver)
        email_page.open()

        email_form = email_page.form
        test_email = 'test.michael@mail.ru'
        email_form.add_email('test.michael@mail.ru')
        email = email_form.get_success()
        self.assert_(email == test_email)
        email_form.close_success()

        email_form.delete_email()
        email_form.close_success()

    def test_not_valid(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        auth_page.top_menu.get_username()

        email_page = EmailPage(self.driver)
        email_page.open()

        email_form = email_page.form
        test_email = 'sheb70017'
        email_form.add_email(test_email)
        error = email_form.check_error()
        self.assert_(error == 'Incorrect email address. Enter a different one.')

    def test_add_email_with_same_name(self):  # возможен ввод в поле резервной почты адреса, совпадающего с адресом основной почты;
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        auth_page.top_menu.get_username()

        email_page = EmailPage(self.driver)
        email_page.open()

        email_form = email_page.form
        test_email = self.LOGIN + '@mail.ru'
        email_form.add_email(test_email)
        email = email_form.get_success()
        self.assert_(email == test_email)  # вообще я искренне удивлен, что оно так работает
        email_form.close_success()
        email_form.delete_email()
        email_form.close_success()

    def test_cancel(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        auth_page.top_menu.get_username()

        email_page = EmailPage(self.driver)
        email_page.open()

        email_form = email_page.form
        email_form.open_adding()
        email_form.cancel()

    def test_delete_success(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        auth_page.top_menu.get_username()

        email_page = EmailPage(self.driver)
        email_page.open()

        email_form = email_page.form
        test_email = 'test.michael@mail.ru'
        email_form.add_email('test.michael@mail.ru')
        email_form.close_success()

        email_form.delete_email()
        mail = email_form.get_success()
        self.assert_(mail == test_email)
        email_form.close_success()
