import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.auth_customer import CustomerAuthPage


class AuthFailedTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.auth_page = CustomerAuthPage(self.driver)
        self.auth_page.open()
        self.EXISTING_USERNAME = os.environ['USERNAME']
        self.NOT_EXISTING_USERNAME = os.environ['USERNAME']
        self.LOGIN = os.environ['LOGIN']
        self.PASSWORD = os.environ['PASSWORD']
