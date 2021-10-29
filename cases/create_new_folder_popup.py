import time
import unittest
import os
from urllib.parse import urlparse
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from steps.default import DefaultSteps
from steps.create_new_folder_popup import CreateNewFolderPopup


class CreateNewFolderPopupTests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)
        DefaultSteps(self.driver).authorize()
        self.steps = CreateNewFolderPopup(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_create_new_folder(self):
        files_before_creation = self.steps.get_amount_of_files()
        self.steps.create_new_folder()
        self.assertTrue(int(files_before_creation) + 1 == int(self.steps.get_amount_of_files()))

    def test_create_new_shared_folder(self):
        files_before_creation = self.steps.get_amount_of_files()
        self.steps.create_new_shared_folder()
        self.assertTrue(int(files_before_creation) + 1 == int(self.steps.get_amount_of_files()))

    def test_create_new_folder_empty_name(self):
        self.steps.create_new_folder_empty_name()
        self.assertEqual(self.steps.errorExists(), True)

    def test_create_new_shared_folder_empty_name(self):
        self.steps.create_new_shared_folder_empty_name()
        self.assertEqual(self.steps.errorExists(), True)

    def test_create_new_folder_long_name(self):
        self.steps.create_new_folder_long_name()
        self.assertEqual(self.steps.errorExists(), True)

    def test_create_new_shared_folder_long_name(self):
        self.steps.create_new_shared_folder_long_name()
        self.assertEqual(self.steps.errorExists(), True)
