import time
import unittest
import os
from urllib.parse import urlparse
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from steps.default import DefaultSteps
from steps.create_new_file import CreateNewFile


class CreateNewFileTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)
        DefaultSteps(self.driver).authorize()
        self.steps = CreateNewFile(self.driver)

    @classmethod
    def tearDownClass(self):
        self.steps.remove_all_files()
        self.driver.quit()

    def tearDown(self):
        self.steps.switch_to_nth_tab(1)
        self.steps.close_current_tab()
        self.steps.switch_to_nth_tab(0)

    def test_create_new_doc(self):
        self.steps.create_new_doc()
        self.assertEqual(len(self.driver.window_handles), 2, 'page with editing new document not opened')

    def test_create_new_table(self):
        self.steps.create_new_table()
        self.assertEqual(len(self.driver.window_handles), 2, 'page with editing new table not opened')

    def test_create_new_pres(self):
        self.steps.create_new_pptx()
        self.assertEqual(len(self.driver.window_handles), 2, 'page with editing new presentation not opened')
