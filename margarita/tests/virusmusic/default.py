import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from margarita.pages.virusmusic.auth import AuthPage


class Test(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        self.assertEqual(
            auth_page.get_navbar_login(),
            os.environ['LOGIN']
        )

    def tearDown(self):
        self.driver.quit()
