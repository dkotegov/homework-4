import unittest

from Pages.auth_page import AuthPage
from tests.default_setup import default_setup
from steps.auth import setup_auth


class LogOutTests(unittest.TestCase):

    def setUp(self):
        default_setup(self)
        self.auth_page = AuthPage(self.driver)
        setup_auth(self)

    def tearDown(self):
        self.driver.quit()

    def test_logout(self):
        self.auth_page.logout()
        self.assertTrue(self.auth_page.not_authorized())
