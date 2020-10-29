import os
import time
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from Auth import AuthPage
from Base import Page


class GetTest(unittest.TestCase):
    def setUp(self) -> None:
        browser = 'CHROME'
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        LOGIN = 'alexersh.test'
        PASSWORD = os.environ['PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)

    def tearDown(self) -> None:
        self.driver.quit()

    def runTest(self):
        home_page = Page(self.driver)
        home_page.open()
