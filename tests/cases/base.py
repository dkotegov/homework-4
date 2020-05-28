import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.auth import AuthPage


class Test(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get("BROWSER", "CHROME")
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
        )

    def tearDown(self):
        self.driver.quit()


class TestAuthorized(Test):
    def setUp(self):
        super().setUp()
        login = os.environ.get("LOGIN")
        password = os.environ.get("PASSWORD")
        auth_page = AuthPage(self.driver)
        auth_page.form.authorise(login, password)