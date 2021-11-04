import time
import unittest
import os
from urllib.parse import urlparse
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from steps.default import DefaultSteps
from steps.file_dropdown_menu import FileDropDownMenu
from pages.file_dropdown_menu import FileDropDownMenuPage


class FileDropDownMenuTests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)
        DefaultSteps(self.driver).authorize()
        self.steps = FileDropDownMenu(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_file_new_tab_open(self):
        self.steps.open_first_file_in_new_tab()
        self.assertTrue(self.steps.compare_file_names(FileDropDownMenuPage.OPENED_NEW_TAB_FILE_NAME), "Wrong file was opened!")

    def test_file_attach_to_mail(self):
        self.steps.send_via_male()
        self.assertTrue(self.steps.compare_file_names(FileDropDownMenuPage.ATTACHED_TO_MAIL_FILE_NAME), "Wrong file was attached!")

    def test_add_to_favorites(self):
        self.steps.add_to_favorites()
        self.assertTrue(self.steps.check_item_in_favorites(), "File has not been added to favorites!")

    def test_rename_empty_string(self):
        self.steps.rename_file_with_empty_string()
        self.assertTrue(self.steps.check_error_exists(), "Error was not showed!")

    def test_rename_long_string(self):
        self.steps.rename_file_with_long_string()
        self.assertTrue(self.steps.check_error_exists(), "Error was not showed!")

    def test_download_file(self):
        self.steps.download_first_file()
        self.assertTrue(self.steps.check_file_downloaded(), "File did not start download!")

    def test_remove_modal(self):
        self.steps.open_modal_remove()
        self.assertTrue(self.steps.check_modal_remove_exists(), "Modal Remove did not open!")
        self.steps.close_modal_remove()
        self.assertFalse(self.steps.check_modal_remove_exists(), "Modal Remove did not closed!")

    def test_remove_to_bin(self):
        self.steps.move_file_to_bin()
