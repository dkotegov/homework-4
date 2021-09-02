import unittest

from test.default_setup import default_setup
from pages.auth_page import AuthPage


class AuthTests(unittest.TestCase):

    def setUp(self):
        default_setup(self)
        self.auth_page = AuthPage(self.driver)
        self.auth_page.open()

    def test_auth_success(self):
        self.auth_page.set_login(self.LOGIN)
        self.auth_page.open_window_sign_in()
        self.auth_page.set_password(self.PASSWORD)
        self.auth_page.submit()
        self.auth_page.open_cloud()
        current_login = self.auth_page.check_log()
        self.assertEqual(self.LOGIN, current_login)

    def tearDown(self):
        self.driver.quit()
