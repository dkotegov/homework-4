import os

import unittest
from tests.default_setup import default_setup
from Pages.signup_page import SignupPage

class SignupWrongTests(unittest.TestCase):
    signup_login = "qqqqqq"
    signup_password = "12345678"
    signup_mail = "qwer@mail.ru"
    signup_login_less_5 = "qqqq"
    signup_password_less_8 = "1234567"
    expected_error_exist_login = "Пользователь с таким логином уже существует"
    expected_error_login_less_5 = "Недопустимый логин(Должен быть от 5 до 15 символов)"
    expected_error_password_less_8 = "Недопустимый пароль(Должен быть от 8 до 16 символов)"
    expected_error_clear_email = "Пустой email"
    empty = ""

    def setUp(self):
        default_setup(self)
        self.signup_page = SignupPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_signup_exist_login(self):
        self.signup_page.open()
        self.signup_page.set_login(self.LOGIN)
        self.signup_page.set_password(self.signup_password)
        self.signup_page.set_mail(self.signup_mail)
        self.signup_page.submit()
        error_msg = self.signup_page.get_error_bad_fields()
        self.assertEqual(error_msg, self.expected_error_exist_login)

    def test_signup_login_less_5_symbols(self):
        self.signup_page.open()
        self.signup_page.set_login(self.signup_login_less_5)
        self.signup_page.set_password(self.signup_password)
        self.signup_page.set_mail(self.signup_mail)
        self.signup_page.submit()
        error_msg = self.signup_page.get_error_bad_login()
        self.assertEqual(error_msg, self.expected_error_login_less_5)

    def test_signup_pass_less_8_symbols(self):
        self.signup_page.open()
        self.signup_page.set_login(self.signup_login)
        self.signup_page.set_password(self.signup_password_less_8)
        self.signup_page.set_mail(self.signup_mail)
        self.signup_page.submit()
        error_msg = self.signup_page.get_error_bad_password()
        self.assertEqual(error_msg, self.expected_error_password_less_8)

    def test_signup_clear_all(self):
        self.signup_page.open()
        self.signup_page.set_login(self.empty)
        self.signup_page.set_password(self.empty)
        self.signup_page.set_mail(self.empty)
        self.signup_page.submit()
        error_msg = self.signup_page.get_error_bad_login()
        self.assertEqual(error_msg, self.expected_error_login_less_5)

    def test_signup_clear_login(self):
        self.signup_page.open()
        self.signup_page.set_login(self.empty)
        self.signup_page.set_password(self.signup_password)
        self.signup_page.set_mail(self.signup_mail)
        self.signup_page.submit()
        error_msg = self.signup_page.get_error_bad_login()
        self.assertEqual(error_msg, self.expected_error_login_less_5)

    def test_signup_clear_password(self):
        self.signup_page.open()
        self.signup_page.set_login(self.signup_login)
        self.signup_page.set_password(self.empty)
        self.signup_page.set_mail(self.signup_mail)
        self.signup_page.submit()
        error_msg = self.signup_page.get_error_bad_password()
        self.assertEqual(error_msg, self.expected_error_password_less_8)

    def test_signup_clear_email(self):
        self.signup_page.open()
        self.signup_page.set_login(self.signup_login)
        self.signup_page.set_password(self.signup_password)
        self.signup_page.set_mail(self.empty)
        self.signup_page.submit()
        error_msg = self.signup_page.get_error_bad_fields()
        self.assertEqual(error_msg, self.expected_error_clear_email)

