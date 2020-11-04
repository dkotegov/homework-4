import tempfile
import unittest
from shutil import copy2

import utils
import os

from Home import HomePage

TXT_FILE = os.path.abspath("./Files/upload.txt")
PDF_FILE = os.path.abspath("./Files/upload.pdf")
JPG_FILE = os.path.abspath("./Files/upload.jpg")
MP3_FILE = os.path.abspath("./Files/upload.mp3")
MP4_FILE = os.path.abspath("./Files/upload.mp4")
BINARY_FILE = os.path.abspath("./Files/upload.pkt")


class UsualUploadTests(unittest.TestCase):
    def _upload_and_move_to_trash(self, testfile_filepath):
        file_ext = utils.get_file_extension(testfile_filepath)

        with tempfile.NamedTemporaryFile(suffix=file_ext) as temp_file:
            temp_filepath = temp_file.name
            copy2(testfile_filepath, temp_filepath)

            home_page = HomePage(self.driver)
            home_page.open()

            home_page.files.upload_file(temp_filepath)

            temp_filename = utils.get_filename(temp_filepath)

            # nickeskov: reload page
            home_page.open()

            is_file_exists = home_page.files.check_if_file_exists(temp_filename)

            self.assertTrue(is_file_exists)

            home_page.files.select_file(temp_filename)
            home_page.files.delete_file_from_toolbar()

    def setUp(self) -> None:
        self.driver = utils.standard_set_up_auth()

    def tearDown(self) -> None:
        utils.standard_tear_down_cleanup(self.driver)

    def test_txt_upload(self):
        self._upload_and_move_to_trash(TXT_FILE)

    def test_pdf_upload(self):
        self._upload_and_move_to_trash(PDF_FILE)

    def test_jpg_upload(self):
        self._upload_and_move_to_trash(JPG_FILE)

    def test_mp3_upload(self):
        self._upload_and_move_to_trash(MP3_FILE)

    def test_mp4_upload(self):
        self._upload_and_move_to_trash(MP4_FILE)

    def test_binary_upload(self):
        self._upload_and_move_to_trash(BINARY_FILE)


class DragAndDropUploadTests(unittest.TestCase):
    def _drag_and_drop_and_move_to_trash(self, testfile_filepath):
        file_ext = utils.get_file_extension(testfile_filepath)

        with tempfile.NamedTemporaryFile(suffix=file_ext) as temp_file:
            temp_filepath = temp_file.name
            copy2(testfile_filepath, temp_filepath)

            home_page = HomePage(self.driver)
            home_page.open()

            home_page.files.drag_and_drop_file_upload(temp_filepath)

            temp_filename = utils.get_filename(temp_filepath)

            # nickeskov: reload page
            home_page.open()

            is_file_exists = home_page.files.check_if_file_exists(temp_filename)

            self.assertTrue(is_file_exists)

            home_page.files.select_file(temp_filename)
            home_page.files.delete_file_from_toolbar()

    def setUp(self) -> None:
        self.driver = utils.standard_set_up_auth()

    def tearDown(self) -> None:
        utils.standard_tear_down_cleanup(self.driver)

    def test_txt_upload(self):
        self._drag_and_drop_and_move_to_trash(TXT_FILE)

    def test_pdf_upload(self):
        self._drag_and_drop_and_move_to_trash(PDF_FILE)

    def test_jpg_upload(self):
        self._drag_and_drop_and_move_to_trash(JPG_FILE)

    def test_mp3_upload(self):
        self._drag_and_drop_and_move_to_trash(MP3_FILE)

    def test_mp4_upload(self):
        self._drag_and_drop_and_move_to_trash(MP4_FILE)

    def test_binary_upload(self):
        self._drag_and_drop_and_move_to_trash(BINARY_FILE)
