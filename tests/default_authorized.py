import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from pages.login import LoginPage


class TestAuthorized(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.auth()

        self.assertEqual(
            auth_page.BASE_URL,
            self.driver.current_url
        )

    def tearDown(self):
        self.driver.quit()
