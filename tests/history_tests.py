import os
import tempfile
import unittest
from shutil import copy2
from selenium.webdriver import DesiredCapabilities, Remote

from Auth import AuthPage
from Home import HomePage
from TrashBin import TrashBinPage


class HistoryTests(unittest.TestCase):
    def setUp(self) -> None:
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        LOGIN = 'alexersh.test'
        PASSWORD = os.environ['PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)

    def tearDown(self) -> None:
        trash_bin_page = TrashBinPage(self.driver)
        trash_bin_page.open()
        trash_bin_page.delete.clear_trash_bin()

        self.driver.quit()

    def test_history_add(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as temp_file:
            copy2('./Files/upload_1.jpg', temp_file.name)
            filename = temp_file.name.split('/')[-1]

            home_page = HomePage(self.driver)
            home_page.open()

            home_page.files.upload_file(temp_file.name)
            home_page.files.select_file(filename)

            home_page.history.open_history()
            self.assertEqual(home_page.history.count_history_files(), 1)
            home_page.history.close_history()

            home_page.files.unselect_file()

            home_page.files.upload_file(temp_file.name)
            home_page.files.select_file(filename)

            home_page.history.open_history()
            self.assertEqual(home_page.history.count_history_files(), 2)
            home_page.history.close_history()

            home_page.files.delete_file()

            temp_file.close()

    def test_history_add_with_delete_from_bin(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as temp_file:
            copy2('./Files/upload_1.jpg', temp_file.name)
            filename = temp_file.name.split('/')[-1]

            home_page = HomePage(self.driver)
            home_page.open()

            home_page.files.upload_file(temp_file.name)
            home_page.files.select_file(filename)

            home_page.history.open_history()
            self.assertEqual(home_page.history.count_history_files(), 1)
            home_page.history.close_history()

            home_page.files.unselect_file()

            home_page.files.upload_file(temp_file.name)
            home_page.files.select_file(filename)

            home_page.history.open_history()
            self.assertEqual(home_page.history.count_history_files(), 2)
            home_page.history.close_history()

            home_page.files.delete_file()

            trash_bin_page = TrashBinPage(self.driver)
            trash_bin_page.open()
            trash_bin_page.delete.clear_trash_bin()

            home_page.open()

            home_page.files.upload_file(temp_file.name)
            home_page.files.select_file(filename)

            home_page.history.open_history()
            self.assertEqual(home_page.history.count_history_files(), 3)
            home_page.history.close_history()

            home_page.files.delete_file()

            temp_file.close()
