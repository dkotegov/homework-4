import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from Auth import AuthPage
from Home import HomePage
from TrashBin import TrashBinPage


class TrashBinTests(unittest.TestCase):
    FOLDER_NAME = "Folder exists"
    NON_EXIST_FOLDER_NAME = "Not exists"

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

        home_page = HomePage(self.driver)
        home_page.open()

        home_page.folders.create_folder(self.FOLDER_NAME)
        home_page.folders.delete_folder()

    def tearDown(self) -> None:
        trash_bin_page = TrashBinPage(self.driver)
        trash_bin_page.open()
        trash_bin_page.delete.clear_trash_bin()

        self.driver.quit()

    def check_restore(self, trash_bin_page: TrashBinPage):
        trash_bin_page.open()

        self.assertFalse(trash_bin_page.utils.check_if_file_exist_by_name(self.FOLDER_NAME))

        home_page = HomePage(self.driver)
        home_page.open()

        self.assertTrue(home_page.folders.check_folder_exists(self.FOLDER_NAME))

        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + self.FOLDER_NAME)
        home_page.folders.delete_folder()

    def check_delete(self, trash_bin_page: TrashBinPage):
        trash_bin_page.open()

        self.assertFalse(trash_bin_page.utils.check_if_file_exist_by_name(self.FOLDER_NAME))

        home_page = HomePage(self.driver)
        home_page.open()

        self.assertFalse(home_page.folders.check_folder_exists(self.FOLDER_NAME))

    def test_move_file_to_trash_bin(self):
        trash_bin_page = TrashBinPage(self.driver)
        trash_bin_page.open()

        self.assertTrue(trash_bin_page.utils.check_if_file_exist_by_name(self.FOLDER_NAME))
        self.assertFalse(trash_bin_page.utils.check_if_file_exist_by_name(self.NON_EXIST_FOLDER_NAME))

        trash_bin_page.delete.clear_trash_bin()

    def test_restore_file_from_toolbar(self):
        trash_bin_page = TrashBinPage(self.driver)
        trash_bin_page.open()

        trash_bin_page.restore.restore_file_from_toolbar(self.FOLDER_NAME)

        self.check_restore(trash_bin_page)

    def test_restore_file_from_menu(self):
        trash_bin_page = TrashBinPage(self.driver)
        trash_bin_page.open()

        trash_bin_page.restore.restore_file_from_menu(self.FOLDER_NAME)

        self.check_restore(trash_bin_page)

    def test_delete_file_from_trash_bin(self):
        trash_bin_page = TrashBinPage(self.driver)
        trash_bin_page.open()

        trash_bin_page.delete.clear_trash_bin()

        self.check_delete(trash_bin_page)
