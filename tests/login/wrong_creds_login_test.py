from pages.login import LoginPage

from tests.default import Test


class WrongCredsLoginTest(Test):
    def test(self):
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.click_login()

        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.auth_with('invalid@invalid.com', 'invalid_password')

        self.assertTrue(auth_page.has_email_error())
        self.assertTrue(auth_page.has_password_error())
