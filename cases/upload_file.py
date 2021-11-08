import time
import unittest
import os
from urllib.parse import urlparse

from selenium.common.exceptions import WebDriverException
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.remote.file_detector import UselessFileDetector
from selenium.webdriver.support.ui import WebDriverWait

from steps.default import DefaultSteps
from steps.upload_file import UploadFile


class UploadFileTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            file_detector = UselessFileDetector()
        )
        self.driver.implicitly_wait(10)
        DefaultSteps(self.driver).authorize()
        self.steps = UploadFile(self.driver)

    @classmethod
    def tearDownClass(self):
        self.steps.remove_all_files()
        self.driver.quit()

    def test_remove_the_restriction_link(self):
        self.steps.click_remove_the_restriction()
        self.assertEqual(len(self.driver.window_handles), 2, 'page with editing new table not opened')