from pages.letter_formatting_page import LetterFormattingPage
from tests.base_test import BaseTest


class BaseSend(BaseTest):
    def test(self):
        BaseTest.test(self)
        self.file_attaching_page = LetterFormattingPage(self.driver)
        self.file_attaching_form = self.file_attaching_page.form
