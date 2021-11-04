import time
import unittest
import os
from urllib.parse import urlparse

from selenium.common.exceptions import WebDriverException
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.remote.file_detector import UselessFileDetector
from selenium.webdriver.support.ui import WebDriverWait

from steps.default import DefaultSteps
from steps.head import Head


class HeadTests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            file_detector=UselessFileDetector()
        )
        self.driver.implicitly_wait(10)
        DefaultSteps(self.driver).authorize()
        self.steps = Head(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_logo(self):
        self.steps.click_logo()
        self.assertEqual(self.driver.current_url, 'https://cloud.mail.ru/home/', '')

    def test_help(self):
        self.steps.click_help()
        self.assertEqual(len(self.driver.window_handles), 2, '')
