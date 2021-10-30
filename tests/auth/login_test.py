import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from pages.auth import AuthPage


class AuthTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.auth()

        self.assertEqual(
            auth_page.BASE_URL,
            self.driver.current_url
        )
