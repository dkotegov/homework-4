import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote

from config import HUB_ADDRESS
from steps.steps import AuthStep

class LoginTest(unittest.TestCase):
    USEREMAIL = os.environ['USEREMAIL']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor=HUB_ADDRESS,
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth = AuthStep(self.driver)
        auth.login(self.USEREMAIL, self.PASSWORD)
