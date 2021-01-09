import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from pages.AuthPage import AuthPage
from selenium.common.exceptions import TimeoutException


class BaseTest(unittest.TestCase):
    """Базовый тестовый класс"""

    def setUp(self):
        try:
            browser = os.environ.get('BROWSER', 'CHROME')
            self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
            )

            self.LOGIN = os.environ['LOGIN']
            self.PASSWORD = os.environ['PASSWORD']

            auth_page = AuthPage(self.driver)
            auth_page.auth(os.environ['LOGIN'], os.environ['PASSWORD'])
        except TimeoutException as e:
            self.driver.quit()
            raise e

    def tearDown(self):
        self.driver.quit()
