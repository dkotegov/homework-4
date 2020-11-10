import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from nikita.pages.todo.auth import AuthPage

class Test(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        authPage = AuthPage(self.driver)
        authPage.auth()
        self.assertEqual(
            authPage.get_navbar_email(),
            os.environ['LOGIN'] + '@mail.ru'
        )

    def tearDown(self):
        self.driver.quit()
