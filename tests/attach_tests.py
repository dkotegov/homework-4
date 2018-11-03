# coding=utf-8
from components.login_and_write import login_and_write

from pages.letter_formatting_page import LetterFormattingPage
from tests.base_test import BaseTest



class AttachTests(BaseTest):
    # ATTACH_FILE_BUTTON =

    TEST_FILE_XLSX = './test_files/АДАМОВА!.xlsx'

    def test(self):
        login_and_write(self.driver, self.USEREMAIL, self.PASSWORD)
        # форматирование письма
        letter_formatting_page = LetterFormattingPage(self.driver)
        letter_formatting_form = letter_formatting_page.form
        letter_formatting_form.open_writing_letter()
        letter_formatting_form.get_file_attach_input().send_keys(self.TEST_FILE_XLSX)
        letter_formatting_form

        self.assertEqual(1,1)
