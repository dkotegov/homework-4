import unittest
from os import environ
from selenium.webdriver import DesiredCapabilities, Remote


class BaseTest(unittest.TestCase):
    def setUp(self):
        browser = environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()
