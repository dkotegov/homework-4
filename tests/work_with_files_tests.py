import os
import time
import unittest
import utils

from Auth import AuthPage
from Home import HomePage
from TrashBin import TrashBinPage


class WorkWithFilesTests(unittest.TestCase):
    TEMP_FOLDER = './Files/tmp/'
    UPLOAD_FILENAME = 'upload_1.jpg'
    UPLOAD_FILE_PATH = './Files/'

    def setUp(self) -> None:
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = utils.get_remote_driver(browser)

        LOGIN = 'alexersh.test'
        PASSWORD = os.environ['PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)

        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.upload_file(self.UPLOAD_FILE_PATH + self.UPLOAD_FILENAME)

    def tearDown(self) -> None:
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.select_file(self.UPLOAD_FILENAME)
        home_page.files.delete_file()

        trash_bin_page = TrashBinPage(self.driver)
        trash_bin_page.open()
        trash_bin_page.delete.clear_trash_bin()

        self.driver.quit()

    def download_from_toolbar(self):
        home_page = HomePage(self.driver)

        home_page.files.select_file(self.UPLOAD_FILENAME)

        home_page.download.download_from_toolbar()
        home_page.download.wait_for_download(self.TEMP_FOLDER, self.UPLOAD_FILENAME)

        self.assertEqual(os.path.exists(self.TEMP_FOLDER + self.UPLOAD_FILENAME), True)

        os.remove(self.TEMP_FOLDER + self.UPLOAD_FILENAME)

    def download_from_context(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.open_context(self.UPLOAD_FILENAME)
        home_page.download.download_from_context()

        home_page.download.wait_for_download(self.TEMP_FOLDER, self.UPLOAD_FILENAME)

        self.assertEqual(os.path.exists(self.TEMP_FOLDER + self.UPLOAD_FILENAME), True)

        os.remove(self.TEMP_FOLDER + self.UPLOAD_FILENAME)

    def test_download_from_grid(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.hover_file(self.UPLOAD_FILENAME)
        home_page.download.download_from_grid(self.UPLOAD_FILENAME)

        home_page.download.wait_for_download(self.TEMP_FOLDER, self.UPLOAD_FILENAME)

        self.assertEqual(os.path.exists(self.TEMP_FOLDER + self.UPLOAD_FILENAME), True)

        os.remove(self.TEMP_FOLDER + self.UPLOAD_FILENAME)
