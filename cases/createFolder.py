import unittest
import os
from urllib.parse import urlparse
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from steps.home import HomeSteps


class CreateFolder(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test(self):
        home = HomeSteps(self.driver)
        home.authorize()
        home.create_folder()
