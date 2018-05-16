import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from src.auth_factory import AuthFactory
from src.pages.auth_page import AuthPage
from src.pages.main_page import MainPage


class MainPageTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self._auth = AuthFactory.create(username='technopark8')

        self.auth_page = AuthPage(self.driver)
        self.main_page = MainPage(self.driver)

        self.auth_page.open()
        self.auth_page.sign_in(self._auth.username, self._auth.password)

    def tearDown(self):
        self.driver.quit()

    def test_open_gifts(self):
        gifts_page = self.main_page.open_gifts()
        ok = gifts_page.is_loaded()
        self.assertTrue(ok)
