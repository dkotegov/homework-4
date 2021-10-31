from .base import BaseTest
from pages.login import LoginPage
from os import environ


class LoginTestSuite(BaseTest):
    def test_success(self):
        page = LoginPage(self.driver)

        page.open()
        page.sign_in()

        self.assertEqual(environ.get('LOGIN', ''), page.get_username_from_profile())

    def test_invalid_login(self):
        page = LoginPage(self.driver)

        page.open()
        page.sign_in('invalidlogin', 'password')

        self.assertEqual('Введен некорректный логин или пароль!', page.validation_hint)

    def test_transition_to_sign_up_from_form(self):
        page = LoginPage(self.driver)

        page.open()
        page.go_to_signup_from_form()

        self.assertEqual(f'{page.ROOT_URL}/signup', self.driver.current_url)

    def test_transition_to_sign_up_from_header(self):
        page = LoginPage(self.driver)

        page.open()
        page.go_to_signup_from_header()

        self.assertEqual(f'{page.ROOT_URL}/signup', self.driver.current_url)
