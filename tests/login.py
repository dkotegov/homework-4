from .base import BaseTest
from pages.login import LoginPage
from os import environ


class LoginTestSuite(BaseTest):
    def test_success(self):
        page = LoginPage(self.driver)

        page.open()
        page.sign_in()

        self.assertEqual(environ.get("LOGIN", ""), page.username_in_profile)

    def test_invalid_login(self):
        page = LoginPage(self.driver)

        page.open()
        page.sign_in('invalidlogin', 'password')

        self.assertEqual('Введен некорректный логин или пароль!', page.validation_hint)
