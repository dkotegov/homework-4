import time
import unittest
import os
from urllib.parse import urlparse

from selenium.common.exceptions import WebDriverException
from selenium.webdriver import DesiredCapabilities, Remote, ChromeOptions
from selenium.webdriver.remote.file_detector import UselessFileDetector
from selenium.webdriver.support.ui import WebDriverWait

from steps.default import DefaultSteps
from steps.toolbar import Toolbar


class ToolbarTests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            file_detector = UselessFileDetector(),
            options = chrome_options
        )
        self.driver.implicitly_wait(10)
        DefaultSteps(self.driver).authorize()
        self.steps = Toolbar(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_select_all(self):
        self.steps.select_all()
        self.assertEqual(self.steps.all_items_selected(), True, '')

    # def test_download_all(self):
    #     self.steps.download_all()
    #     time.sleep(1)
    #     # self.assertEqual(len(self.driver.window_handles), 2, 'page with editing new table not opened')