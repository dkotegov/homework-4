from .base import BaseTest
from pages.signup import SignupPage
from os import environ


class SignupTestSuite(BaseTest):
    def test_transition_to_login_from_form(self):
        page = SignupPage(self.driver)

        page.open()
        page.go_to_login_from_form()

        self.assertEqual(f'{page.ROOT_URL}/login', self.driver.current_url)

    def test_transition_to_login_from_header(self):
        page = SignupPage(self.driver)

        page.open()
        page.go_to_login_from_header()

        self.assertEqual(f'{page.ROOT_URL}/login', self.driver.current_url)
