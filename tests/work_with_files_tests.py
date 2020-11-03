import os
import time
import unittest
import utils

from Auth import AuthPage
from Home import HomePage
from Favorites import FavoritePage
from TrashBin import TrashBinPage


class WorkWithFilesTests(unittest.TestCase):
    TEMP_FOLDER = './Files/tmp/'
    UPLOAD_FILENAME = 'upload_1.jpg'
    NEW_UPLOAD_FILENAME = 'upload'
    UPLOAD_FILE_PATH = './Files/'
    COPY_AND_MOVE_FOLDER = 'Temp'

    def setUp(self) -> None:
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = utils.get_remote_driver(browser)

        LOGIN = 'alexersh.testing'
        PASSWORD = os.environ['PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)

        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.upload_file(self.UPLOAD_FILE_PATH + self.UPLOAD_FILENAME)

    def tearDown(self) -> None:
        home_page = HomePage(self.driver)
        home_page.open()

        exists = home_page.files.select_file_if_exists(self.UPLOAD_FILENAME)
        if exists:
            home_page.files.delete_file_from_toolbar()

        exists = home_page.files.select_file_if_exists(
            self.NEW_UPLOAD_FILENAME + '.' + self.UPLOAD_FILENAME.split('.')[-1])
        if exists:
            home_page.files.delete_file_from_toolbar()

        trash_bin_page = TrashBinPage(self.driver)
        trash_bin_page.open()
        trash_bin_page.delete.clear_trash_bin()

        self.driver.quit()

    def test_download_from_toolbar(self):
        home_page = HomePage(self.driver)

        home_page.files.select_file(self.UPLOAD_FILENAME)

        home_page.download.download_from_toolbar()
        home_page.download.wait_for_download(self.TEMP_FOLDER, self.UPLOAD_FILENAME)

        self.assertEqual(os.path.exists(self.TEMP_FOLDER + self.UPLOAD_FILENAME), True)

        os.remove(self.TEMP_FOLDER + self.UPLOAD_FILENAME)

    def test_download_from_context(self):
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

    def test_favorites_add_and_remove_from_toolbar(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.select_file(self.UPLOAD_FILENAME)
        home_page.favorites.add_in_toolbar()

        fav_page = FavoritePage(self.driver)
        fav_page.open()

        self.assertTrue(fav_page.utils.check_if_file_exists(self.UPLOAD_FILENAME))

        home_page.open()

        home_page.files.select_file(self.UPLOAD_FILENAME)
        home_page.favorites.remove_in_toolbar()

        fav_page.open()

        self.assertFalse(fav_page.utils.check_if_file_exists(self.UPLOAD_FILENAME))

    def test_favorites_add_and_remove_from_context(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.open_context(self.UPLOAD_FILENAME)
        home_page.favorites.add_in_context()

        fav_page = FavoritePage(self.driver)
        fav_page.open()

        self.assertTrue(fav_page.utils.check_if_file_exists(self.UPLOAD_FILENAME))

        home_page.open()

        home_page.files.open_context(self.UPLOAD_FILENAME)
        home_page.favorites.remove_in_context()

        fav_page.open()

        self.assertFalse(fav_page.utils.check_if_file_exists(self.UPLOAD_FILENAME))

    def test_favorites_add_and_remove_from_grid(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.hover_file(self.UPLOAD_FILENAME)
        home_page.favorites.add_in_grid(self.UPLOAD_FILENAME)

        fav_page = FavoritePage(self.driver)
        fav_page.open()

        self.assertTrue(fav_page.utils.check_if_file_exists(self.UPLOAD_FILENAME))

        home_page.open()

        home_page.files.hover_file(self.UPLOAD_FILENAME)
        home_page.favorites.remove_in_grid(self.UPLOAD_FILENAME)

        fav_page.open()

        self.assertFalse(fav_page.utils.check_if_file_exists(self.UPLOAD_FILENAME))

    def test_open_history_from_toolbar(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.select_file(self.UPLOAD_FILENAME)
        home_page.history.open_history_from_toolbar()

        self.assertTrue(home_page.history.check_if_history_open())

        home_page.history.close_history()

        self.assertFalse(home_page.history.check_if_history_open())

    def test_open_history_from_context(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.open_context(self.UPLOAD_FILENAME)
        home_page.history.open_history_from_context()

        self.assertTrue(home_page.history.check_if_history_open())

        home_page.history.close_history()

        self.assertFalse(home_page.history.check_if_history_open())

    def test_delete_from_toolbar(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.select_file(self.UPLOAD_FILENAME)
        home_page.files.delete_file_from_toolbar()

        bin_page = TrashBinPage(self.driver)
        bin_page.open()

        self.assertTrue(bin_page.utils.check_if_file_exist_by_name(self.UPLOAD_FILENAME))

    def test_delete_from_context(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.open_context(self.UPLOAD_FILENAME)
        home_page.files.delete_file_from_context()

        bin_page = TrashBinPage(self.driver)
        bin_page.open()

        self.assertTrue(bin_page.utils.check_if_file_exist_by_name(self.UPLOAD_FILENAME))

    def test_copy_from_toolbar(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.folders.create_folder(self.COPY_AND_MOVE_FOLDER)
        home_page.open()

        home_page.files.select_file(self.UPLOAD_FILENAME)
        home_page.copy.copy_from_toolbar(self.COPY_AND_MOVE_FOLDER)

        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + self.COPY_AND_MOVE_FOLDER)
        home_page.files.check_if_file_exists(self.UPLOAD_FILENAME)
        home_page.folders.delete_folder()

    def test_copy_from_context(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.folders.create_folder(self.COPY_AND_MOVE_FOLDER)
        home_page.open()

        home_page.files.open_context(self.UPLOAD_FILENAME)
        home_page.copy.copy_from_context(self.COPY_AND_MOVE_FOLDER)

        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + self.COPY_AND_MOVE_FOLDER)
        home_page.files.check_if_file_exists(self.UPLOAD_FILENAME)
        home_page.folders.delete_folder()

    def test_move_from_toolbar(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.folders.create_folder(self.COPY_AND_MOVE_FOLDER)
        home_page.open()

        home_page.files.select_file(self.UPLOAD_FILENAME)
        home_page.move.move_from_toolbar(self.COPY_AND_MOVE_FOLDER)

        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + self.COPY_AND_MOVE_FOLDER)
        home_page.files.check_if_file_exists(self.UPLOAD_FILENAME)
        home_page.folders.delete_folder()

    def test_move_from_context(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.folders.create_folder(self.COPY_AND_MOVE_FOLDER)
        home_page.open()

        home_page.files.open_context(self.UPLOAD_FILENAME)
        home_page.move.move_from_context(self.COPY_AND_MOVE_FOLDER)

        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + self.COPY_AND_MOVE_FOLDER)
        home_page.files.check_if_file_exists(self.UPLOAD_FILENAME)
        home_page.folders.delete_folder()

    def test_rename_from_toolbar(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.select_file(self.UPLOAD_FILENAME)
        home_page.rename.rename_file_from_toolbar(self.NEW_UPLOAD_FILENAME)

        self.assertTrue(
            home_page.files.check_if_file_exists(self.NEW_UPLOAD_FILENAME + '.' + self.UPLOAD_FILENAME.split('.')[-1]))
        self.assertFalse(home_page.files.check_if_file_exists(self.UPLOAD_FILENAME))

    def test_rename_from_context(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.open_context(self.UPLOAD_FILENAME)
        home_page.rename.rename_file_from_context(self.NEW_UPLOAD_FILENAME)

        self.assertTrue(
            home_page.files.check_if_file_exists(self.NEW_UPLOAD_FILENAME + '.' + self.UPLOAD_FILENAME.split('.')[-1]))
        self.assertFalse(home_page.files.check_if_file_exists(self.UPLOAD_FILENAME))

    def test_share_from_toolbar(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.select_file(self.UPLOAD_FILENAME)
        home_page.share.share_from_toolbar()

        self.assertTrue(home_page.share.check_if_shared())

        home_page.share.stop_share()

        self.assertFalse(home_page.share.check_if_shared())

    def test_share_from_context(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.open_context(self.UPLOAD_FILENAME)
        home_page.share.share_from_context()

        self.assertTrue(home_page.share.check_if_shared())

        home_page.share.stop_share()

        self.assertFalse(home_page.share.check_if_shared())

    def test_share_from_grid(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.files.hover_file(self.UPLOAD_FILENAME)
        home_page.share.share_from_grid(self.UPLOAD_FILENAME)

        self.assertTrue(home_page.share.check_if_shared())

        home_page.share.stop_share()

        self.assertFalse(home_page.share.check_if_shared())
