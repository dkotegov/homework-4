import time
import unittest
import os
from urllib.parse import urlparse
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from steps.default import DefaultSteps
from steps.toolbar_create_new_file import ToolbarCreateNewFile


class ToolbarCreateNewFileTests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)
        DefaultSteps(self.driver).authorize()
        self.steps = ToolbarCreateNewFile(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_create_new_folder(self):
        self.steps.create_new_folder()
        self.assertTrue(self.steps.check_modal_exists(), "Modal was not shown")

    def test_create_new_docx(self):
        self.steps.create_new_docx()
        self.assertEqual(len(self.driver.window_handles), 2, 'page with editing new document not opened')

    def test_create_new_table(self):
        self.steps.test_create_new_table()
        self.assertEqual(len(self.driver.window_handles), 2, 'page with editing new document not opened')

    def test_create_new_presentation(self):
        self.steps.test_create_new_presentation()
        self.assertEqual(len(self.driver.window_handles), 2, 'page with editing new document not opened')


