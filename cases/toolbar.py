import time
import unittest
import os
from urllib.parse import urlparse

from selenium.common.exceptions import WebDriverException
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.remote.file_detector import UselessFileDetector
from selenium.webdriver.support.ui import WebDriverWait

from steps.default import DefaultSteps
from steps.toolbar import Toolbar


class ToolbarTests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            file_detector = UselessFileDetector()
        )
        self.driver.implicitly_wait(10)
        DefaultSteps(self.driver).authorize()
        self.steps = Toolbar(self.driver)

    def tearDown(self):
        self.driver.quit()

    # def test_upload_normal_file(self):
    #     file_path = '/Users/ivankovalenko/PycharmProjects/qa/homework-4/all_keys.txt'
    #     self.steps.upload_file(file_path)
    #     self.assertEqual(self.steps.error_exists(), False, '')
    #
    # def test_upload_big_file(self):
    #     # file_path = '/Users/ivankovalenko/Downloads/GMT20211014-151110_Recording_3840x2160.mp4'
    #     file_path = '/Users/ivankovalenko/PycharmProjects/qa/homework-4/test.txt'
    #     self.steps.upload_file(file_path)
    #     self.assertEqual(self.steps.error_exists(), True, '')

    def test_select_all(self):
        self.steps.select_all()
        time.sleep(5)
        # self.assertEqual(len(self.driver.window_handles), 2, 'page with editing new table not opened')