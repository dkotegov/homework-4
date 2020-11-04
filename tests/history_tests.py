import tempfile
import unittest
from shutil import copy2


import utils
from Home import HomePage
from TrashBin import TrashBinPage


class HistoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = utils.standard_set_up_auth()

    def tearDown(self) -> None:
        utils.standard_tear_down_cleanup(self.driver)

    def test_history_add(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as temp_file:
            copy2('./Files/upload_1.jpg', temp_file.name)
            filename = temp_file.name.split('/')[-1]

            home_page = HomePage(self.driver)
            home_page.open()

            home_page.files.upload_file(temp_file.name)
            home_page.files.select_file(filename)

            home_page.history.open_history_from_toolbar()
            self.assertEqual(home_page.history.count_history_files(), 1)
            home_page.history.close_history()

            home_page.files.unselect_file()

            home_page.files.upload_file(temp_file.name)
            home_page.files.select_file(filename)

            home_page.history.open_history_from_toolbar()
            self.assertEqual(home_page.history.count_history_files(), 2)
            home_page.history.close_history()

            home_page.files.delete_file_from_toolbar()

            temp_file.close()

    def test_history_add_with_delete_from_bin(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as temp_file:
            copy2('./Files/upload_1.jpg', temp_file.name)
            filename = temp_file.name.split('/')[-1]

            home_page = HomePage(self.driver)
            home_page.open()

            home_page.files.upload_file(temp_file.name)
            home_page.files.select_file(filename)

            home_page.history.open_history_from_toolbar()
            self.assertEqual(home_page.history.count_history_files(), 1)
            home_page.history.close_history()

            home_page.files.unselect_file()

            home_page.files.upload_file(temp_file.name)
            home_page.files.select_file(filename)

            home_page.history.open_history_from_toolbar()
            self.assertEqual(home_page.history.count_history_files(), 2)
            home_page.history.close_history()

            home_page.files.delete_file_from_toolbar()

            trash_bin_page = TrashBinPage(self.driver)
            trash_bin_page.open()
            trash_bin_page.delete.clear_trash_bin()

            home_page.open()

            home_page.files.upload_file(temp_file.name)
            home_page.files.select_file(filename)

            home_page.history.open_history_from_toolbar()
            self.assertEqual(home_page.history.count_history_files(), 3)
            home_page.history.close_history()

            home_page.files.delete_file_from_toolbar()

            temp_file.close()
