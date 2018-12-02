from pages.file_attaching_page import FileAttachingPage
from tests.base_test import BaseTest


class BaseAttach(BaseTest):
    TEST_FILE_DIR = './test_files/'

    def test(self):
        BaseTest.test(self)
        self.file_attaching_page = FileAttachingPage(self.driver)
        self.file_attaching_form = self.file_attaching_page.form
        self.file_attaching_page.redirectQA()
