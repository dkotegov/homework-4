import unittest
from tests.default_setup import default_setup
from Pages.settings_page import SettingPage
from steps.auth import setup_auth


class UsernameChangeWrongTests(unittest.TestCase):
    exist_login = "TestUser"
    login_less5 = "123"
    login_more15 = "12345678901234561"
    expected_error_exist_login = "Пользователь с таким логином уже существует"
    expected_error_less_or_more_login = "Недопустимый логин(Должен быть от 5 до 15 символов)"
    empty_form = ""

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.setting_page = SettingPage(self.driver)
        self.setting_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_change_login_exist(self):
        self.setting_page.set_username(self.exist_login)
        self.setting_page.submit()
        error_msg = self.setting_page.get_main_error()
        self.assertEqual(error_msg, self.expected_error_exist_login)

    def test_change_login_less5(self):
        self.setting_page.set_username(self.login_less5)
        self.setting_page.set_old_pass(self.empty_form)
        error_msg = self.setting_page.get_login_error()
        self.assertEqual(error_msg, self.expected_error_less_or_more_login)

    def test_change_login_more15(self):
        self.setting_page.set_username(self.login_more15)
        self.setting_page.set_old_pass(self.empty_form)
        error_msg = self.setting_page.get_login_error()
        self.assertEqual(error_msg, self.expected_error_less_or_more_login)
