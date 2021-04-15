import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from tests.folder_tests.src.auth_page import AuthPage
from tests.folder_tests.src.main_page import MainPage


class PasswordTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ['BROWSER']

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_1_success_short(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        main_page = MainPage(self.driver)
        main_form = main_page.main_form
        main_form.open_folder_editor()

        edit_form = main_page.edit_folder_form
        edit_form.protected_by_password()
        edit_form.set_password_popup()
        edit_form.set_password('123', '123', 'qqq', 'aaa', self.PASSWORD)

    def test_2_success_long(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        main_page = MainPage(self.driver)
        main_form = main_page.main_form
        main_form.open_folder_editor()

        edit_form = main_page.edit_folder_form

        edit_form.protected_by_password()
        edit_form.set_password_popup()
        edit_form.set_password('123' * 11, '123' * 11, 'qqq', 'aaa', self.PASSWORD)

    def test_3_wrong_pwd(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        main_page = MainPage(self.driver)
        main_form = main_page.main_form
        main_form.open_folder_editor()

        edit_form = main_page.edit_folder_form

        edit_form.protected_by_password()
        edit_form.set_password_popup()
        edit_form.set_password('12345', '1234', 'qqq', 'aaa', self.PASSWORD)

    def test_4_success(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        main_page = MainPage(self.driver)
        main_form = main_page.main_form
        main_form.open_folder_editor()

        edit_form = main_page.edit_folder_form
        edit_form.unavailable_pop3()
        edit_form.protected_by_password()
        edit_form.set_password_popup()
        edit_form.set_password('1234', '1234', 'qqq', 'aaa', self.PASSWORD)

    def test_5_remove_pwd(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        main_page = MainPage(self.driver)
        main_form = main_page.main_form
        main_form.open_folder_editor()

        edit_form = main_page.edit_password_form
        edit_form.set_folder_password('1234')
        edit_form.next_popup()
        edit_form.remove_password_click()
        edit_form.set_user_password(self.PASSWORD)
        edit_form.remove_password_submit()
