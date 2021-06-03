import os

import unittest
from tests.default_setup import default_setup
from Pages.auth_page import AuthPage
from steps.get_profile_login import get_profile_login


class AuthWrongTests(unittest.TestCase):
    auth_correct_login = os.environ["LOGIN"]
    auth_correct_password = os.environ["PASSWORD"]
    auth_wrong_login = "qqqqqq"
    auth_wrong_password = "12345678"
    expected_error_wrong_login = "Неправильное имя пользователя или пароль"
    expected_error_wrong_password = "Неправильное имя пользователя или пароль"
    expected_error_empty_login = "Пустой логин"
    expected_error_empty_password = "Пустой пароль"
    empty_field = ""

    def setUp(self):
        default_setup(self)
        self.auth_page = AuthPage(self.driver)
        self.auth_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_wrong_login(self):
        self.auth_page.set_login(self.auth_wrong_login)
        self.auth_page.set_password(self.auth_correct_password)
        self.auth_page.submit()
        error_msg = self.auth_page.get_current_error()
        self.assertEqual(error_msg, self.expected_error_wrong_login)

    def test_wrong_password(self):
        self.auth_page.set_login(self.auth_correct_login)
        self.auth_page.set_password(self.auth_wrong_password)
        self.auth_page.submit()
        error_msg = self.auth_page.get_current_error()
        self.assertEqual(error_msg, self.expected_error_wrong_password)

    def test_empty_login(self):
        self.auth_page.set_login(self.empty_field)
        self.auth_page.set_password(self.auth_correct_password)
        self.auth_page.submit()
        error_msg = self.auth_page.get_current_error()
        self.assertEqual(error_msg, self.expected_error_empty_login)

    def test_empty_password(self):
        self.auth_page.set_login(self.auth_correct_login)
        self.auth_page.set_password(self.empty_field)
        self.auth_page.submit()
        error_msg = self.auth_page.get_current_error()
        self.assertEqual(error_msg, self.expected_error_empty_password)

    def test_empty_login_and_password(self):
        self.auth_page.set_login(self.empty_field)
        self.auth_page.set_password(self.empty_field)
        self.auth_page.submit()
        error_msg = self.auth_page.get_current_error()
        self.assertEqual(error_msg, self.expected_error_empty_login)
