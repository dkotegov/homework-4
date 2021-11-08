import time
import unittest
import os
from urllib.parse import urlparse
from selenium.webdriver import DesiredCapabilities, Remote, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait

from steps.toolbar_sort import ToolbarSortFiles
from steps.search_file import SearchFile
from steps.default import DefaultSteps


class ToolbarSortFilesTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            options=chrome_options
        )
        self.driver.implicitly_wait(10)
        DefaultSteps(self.driver).authorize()
        self.steps = ToolbarSortFiles(self.driver)
        steps_load_file = SearchFile(self.driver)
        steps_load_file.load_test_file('c.txt')
        steps_load_file.load_test_file('b.txt')
        steps_load_file.load_test_file('a.txt')

    @classmethod
    def tearDownClass(self):
        self.steps.remove_all_files()
        self.driver.quit()

    def test_alphabet_asc(self):
        self.steps.sort_by_alphabet_asc()
        self.assertTrue(self.steps.check_correct_order(self.steps.page.ALPHABETIC_ASC_ORDER), "Incorrect alphabet "
                                                                                              "ascending sort!")

    def test_alphabet_desc(self):
        self.steps.sort_by_alphabet_desc()
        self.assertTrue(self.steps.check_correct_order(self.steps.page.ALPHABETIC_DESC_ORDER), "Incorrect alphabet "
                                                                                               "descending sort!")

    def test_size_asc(self):
        self.steps.sort_by_size_asc()
        self.assertTrue(self.steps.check_correct_order(self.steps.page.SIZE_ASC_ORDER), "Incorrect size "
                                                                                        "ascending sort!")

    def test_size_desc(self):
        self.steps.sort_by_size_desc()
        self.assertTrue(self.steps.check_correct_order(self.steps.page.SIZE_DESC_ORDER), "Incorrect size descending "
                                                                                         "sort!")

    def test_date_asc(self):
        self.steps.sort_by_date_asc()
        self.assertTrue(self.steps.check_correct_order(self.steps.page.DATE_ASC_ORDER), "Incorrect date "
                                                                                        "ascending sort!")

    def test_date_desc(self):
        self.steps.sort_by_date_desc()
        self.assertTrue(self.steps.check_correct_order(self.steps.page.DATE_DESC_ORDER), "Incorrect date "
                                                                                         "descending sort!")


