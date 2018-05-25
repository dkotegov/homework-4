import unittest
import os

from tests.pages.primary.auth_page import AuthPage
from util import config

from selenium.webdriver import DesiredCapabilities, Remote


class BasicTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get(config.PREFERRED_BROWSER_KEY, config.PREF_FIREFOX)
        self.driver = Remote(command_executor=config.SELENIUM_GRID_HUB_ADDRESS,
                             desired_capabilities=getattr(DesiredCapabilities, browser).copy())
        self.auth()

    def tearDown(self):
        self.driver.quit()

    def auth(self):
        auth = AuthPage(self.driver)
        auth.open()
        form = auth.form
        form.set_login(config.TEST_LOGIN)
        form.set_password(config.TEST_PASSWORD)
        form.submit()
