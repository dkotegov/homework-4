import unittest
from tests.default_setup import default_setup
from Pages.settings_page import SettingPage
from steps.auth import setup_auth


class PasswordChangeWrongTests(unittest.TestCase):
    new_password = "Arkady123"
    password_less8 = "Ark"
    password_more16 = "arkadiyarkadiyarkadiy"
    different_new_password = "Arkady124"
    wrong_old_password = "wrong_old"
    expected_error_wrong_old_password = "Неправильный старый пароль"
    expected_error_different_new_password = "Пароли не совпадают"
    expected_error_less_or_more_password = "Недопустимый первый пароль(Должен быть от 8 до 16 символов)"

    def setUp(self):
        default_setup(self)
        self.old_password = self.PASSWORD
        setup_auth(self)
        self.setting_page = SettingPage(self.driver)
        self.setting_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_change_password_wrong_old(self):
        self.setting_page.set_old_pass(self.wrong_old_password)
        self.setting_page.set_new_pass(self.new_password)
        self.setting_page.set_new_pass_confirm(self.new_password)
        self.setting_page.submit()
        error_msg = self.setting_page.get_main_error()
        self.assertEqual(error_msg, self.expected_error_wrong_old_password)

    def test_change_password_different_new(self):
        self.setting_page.set_old_pass(self.old_password)
        self.setting_page.set_new_pass(self.new_password)
        self.setting_page.set_new_pass_confirm(self.different_new_password)
        self.setting_page.submit()
        error_msg = self.setting_page.get_password_diff_error()
        self.assertEqual(error_msg, self.expected_error_different_new_password)

    def test_change_password_new_less8(self):
        self.setting_page.set_old_pass(self.old_password)
        self.setting_page.set_new_pass(self.password_less8)
        self.setting_page.set_new_pass_confirm(self.password_less8)
        error_msg = self.setting_page.get_password_error()
        self.assertEqual(error_msg, self.expected_error_less_or_more_password)

    def test_change_password_new_more16(self):
        self.setting_page.set_old_pass(self.old_password)
        self.setting_page.set_new_pass(self.password_more16)
        self.setting_page.set_new_pass_confirm(self.password_more16)
        error_msg = self.setting_page.get_password_error()
        self.assertEqual(error_msg, self.expected_error_less_or_more_password)
