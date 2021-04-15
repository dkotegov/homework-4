import unittest

from pages.main_page import MainPage
from setup.default_setup import default_setup


class CheckAuth(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.page = MainPage(self.driver)
        self.page.open()

    def test_check_auth(self):
        self.page.open_auth_popup()
        self.page.auth(self.EMAIL, self.PASSWORD)
        is_all_right = self.page.check_auth()
        self.assertTrue(is_all_right)

    def test_check_exit(self):
        self.page.open_auth_popup()
        self.page.auth(self.EMAIL, self.PASSWORD)
        is_all_right = self.page.check_auth()
        self.assertTrue(is_all_right)
        self.page.open_exit_popup()
        self.page.check_exit()
    
    def test_check_wrong_passwrd_auth(self):
        self.page.open_auth_popup()
        self.page.auth(self.EMAIL, "wrong_password")
        is_all_right = self.page.check_auth_password_error("Неверный пароль")
        self.assertTrue(is_all_right)

    def test_check_empty_password_auth(self):
        self.page.open_auth_popup()
        self.page.auth(self.EMAIL, "")
        is_all_right = self.page.check_auth_password_error("Пароль должен содержать не менее 6 символов")
        self.assertTrue(is_all_right)

    def test_check_unexisting_account_auth(self):
        self.page.open_auth_popup()
        self.page.auth("wrong_email@mail.ru", "wrong_password")
        is_all_right = self.page.check_auth_email_error("Такого пользователя не существует")
        self.assertTrue(is_all_right)

    def test_check_empty_email_auth(self):
        self.page.open_auth_popup()
        self.page.auth("", self.PASSWORD)
        is_all_right = self.page.check_auth_email_error("Введите E-mail")
        self.assertTrue(is_all_right)

    def test_check_wrong_format_email_auth(self):
        self.page.open_auth_popup()
        self.page.auth("wrong_emailmail.ru", self.PASSWORD)
        is_all_right = self.page.check_auth_email_error("Неправильный формат E-mail")
        self.assertTrue(is_all_right)

    def test_check_move_to_registration(self):
        self.page.open_auth_popup()
        self.page.move_to_reg_popup()
        is_all_right = self.page.check_reg_popup_appearance()
        self.assertTrue(is_all_right)

    def tearDown(self):
        self.driver.quit()
