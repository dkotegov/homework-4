import time
import unittest
import os
from urllib.parse import urlparse
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from steps.default import DefaultSteps
from steps.search_file import SearchFile

class SearchFileTests(unittest.TestCase):
    TEST_FILENAME = 'test'
    TEST_NONEXISTENT_FILENAME = 'kek'
    TEST_SEARCH_FILE_TYPE = 'Документы'

    @classmethod
    def setUpClass(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)
        DefaultSteps(self.driver).authorize()
        self.steps = SearchFile(self.driver)
        self.steps.load_test_file(self.TEST_FILENAME)
        self.search_types = ['Музыка', 'Видео', 'Документы', 'Файлы PDF', 'Таблицы', 'Презентации', 'Архивы', 'Папки']

    @classmethod
    def tearDownClass(self):
        self.steps.remove_all_files()
        self.driver.quit()

    def test_search_empty_string(self):
        self.steps.search_empty_string()
        self.assertTrue(self.steps.check_search_result_is_empty(), "Search doesn't work with empty string")

    def test_search_uploaded_file(self):
        self.steps.search_uploaded_file(self.TEST_FILENAME)
        self.assertTrue(self.steps.check_search_file_is_found(self.TEST_FILENAME), "Search doesn't find uploaded file")

    def test_search_uploaded_file_with_type(self):
        self.steps.search_uploaded_file_with_type(self.TEST_FILENAME, self.TEST_SEARCH_FILE_TYPE)
        self.assertTrue(self.steps.check_search_file_is_found(self.TEST_FILENAME), "Search doesn't find uploaded file "
                                                                                   "with type")

    def test_search_nonexistent_file_with_type(self):
        self.steps.search_nonexistent_file_with_type(self.TEST_NONEXISTENT_FILENAME, self.TEST_SEARCH_FILE_TYPE)
        self.assertFalse(self.steps.check_search_file_is_found(self.TEST_SEARCH_FILE_TYPE), "Search find nonexistent "
                                                                                            "file with type")

    def test_select_search_type(self):
        for search_type in self.search_types:
            self.steps.select_search_type(search_type)
            self.assertTrue(self.steps.check_selected_type(search_type), "Can't select type")
