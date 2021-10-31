import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from pages.login import LoginPage

from tests.default import Test


class LoginTest(Test):
    def test(self):
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.auth()

        self.assertEqual(
            auth_page.BASE_URL,
            self.driver.current_url
        )
