import unittest

from pages.main_page import MainPage
from setup.default_setup import default_setup
import uuid


class CheckRegist(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.page = MainPage(self.driver)
        self.page.open()

    def test_check_reg(self):
        self.page.open_reg_popup()
        self.page.regist(str(uuid.uuid4()) + '@mail.ru', self.PASSWORD, self.PASSWORD)
        is_all_right = self.page.check_registr()
        self.assertTrue(is_all_right)

    def test_check_invalid_mail(self):
        self.page.open_reg_popup()
        self.page.regist(str(uuid.uuid4()), self.PASSWORD, self.PASSWORD)
        is_all_right = self.page.check_regist_email_error("Неправильный формат E-mail")
        self.assertTrue(is_all_right)

    def test_check_invalid_password_short(self):
        self.page.open_reg_popup()
        self.page.regist(str(uuid.uuid4()), '1111', '1111')
        is_all_right = self.page.check_regist_password_error("Пароль должен содержать не менее 6 символов")
        self.assertTrue(is_all_right)

    def test_check_invalid_repeated_password(self):
        self.page.open_reg_popup()
        self.page.regist(str(uuid.uuid4()) + '@mail.ru', '11111111', '2222222')
        is_all_right = self.page.check_repeated_regist_password_error("Пароли не совпадают")
        self.assertTrue(is_all_right)

    def test_check_exist_mail(self):
        self.page.open_reg_popup()
        self.page.regist(self.EMAIL, self.PASSWORD, self.PASSWORD)
        is_all_right = self.page.check_regist_email_error("Данный Email адрес уже существует")
        self.assertTrue(is_all_right)

    def test_check_empty_mail(self):
        self.page.open_reg_popup()
        self.page.regist('', self.PASSWORD, self.PASSWORD)
        is_all_right = self.page.check_regist_email_error("Введите E-mail")
        self.assertTrue(is_all_right)

    def test_check_empty_password(self):
        self.page.open_reg_popup()
        self.page.regist(str(uuid.uuid4()) + '@mail.ru', '', self.PASSWORD)
        is_all_right = self.page.check_regist_password_error("Пароль должен содержать не менее 6 символов")
        self.assertTrue(is_all_right)

    def test_check_empty_repeated_password(self):
        self.page.open_reg_popup()
        self.page.regist(str(uuid.uuid4()) + '@mail.ru', self.PASSWORD, '')
        is_all_right = self.page.check_repeated_regist_password_error("Пароли не совпадаю")
        self.assertTrue(is_all_right)

    def test_switch_to_auth(self):
        self.page.open_reg_popup()
        is_all_right = self.page.check_auth_popup_appear()
        self.assertTrue(is_all_right)

    def test_close_reg_popup(self):
        self.page.open_reg_popup()
        is_all_right = self.page.check_closed_popup()
        self.assertTrue(is_all_right)

    def tearDown(self):
        self.driver.quit()
