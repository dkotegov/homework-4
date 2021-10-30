from pages.login import LoginPage
from tests.base import BaseTest
from os import environ


class LoginSuccessTest(BaseTest):
    def test(self):
        page = LoginPage(self.driver)

        page.open()
        page.sign_in(self.driver)

        self.assertEqual(environ.get("LOGIN", ""), page.username_in_profile)
