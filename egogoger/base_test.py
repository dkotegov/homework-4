import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
