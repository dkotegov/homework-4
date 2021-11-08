import time
import unittest
import os
from urllib.parse import urlparse
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from steps.default import DefaultSteps
from steps.create_new_file import CreateNewFile
from steps.hover_over_file import HoverOverFile


class HoverOverFileTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)
        DefaultSteps(self.driver).authorize()
        self.steps = HoverOverFile(self.driver)
        self.steps_create_new_file = CreateNewFile(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def tearDown(self):
        self.steps.remove_all_files()

    def test_add_to_favorites(self):
        self.steps_create_new_file.create_new_doc()
        self.steps.add_to_favorites_first_file()
        self.assertTrue(self.steps.check_file_in_favorites(), "Item has not been added to favorites!")

    def test_remove_from_favorites(self):
        self.steps_create_new_file.create_new_doc()
        self.steps.add_to_favorites_first_file()
        self.assertTrue(self.steps.check_file_in_favorites(), "Item has not been added to favorites!")
        self.steps.remove_first_file_from_favorites()
        self.assertFalse(self.steps.check_file_in_favorites(), "Item still in favorites!")

    def test_file_downloading(self):
        self.steps_create_new_file.create_new_doc()
        self.steps.download_first_file()
        self.assertTrue(self.steps.check_file_downloaded(), "File not started downloading!")
