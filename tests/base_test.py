import os
import unittest

from components.login_and_write import login_and_write
from selenium.webdriver import DesiredCapabilities, Remote
from pages.letter_formatting_page import LetterFormattingPage
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
        )

    def tearDown(self):
        self.driver.quit()