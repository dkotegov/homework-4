# coding=utf-8
import os
import unittest

from components.login_and_write import login_and_write
from selenium.webdriver import DesiredCapabilities, Remote
from pages.letter_formatting_page import LetterFormattingPage
from tests.base_test import BaseTest


class LetterFormattingTests(BaseTest):
    USEREMAIL = 'park.test.testovich@mail.ru'
    PASSWORD = 'rha_the_best_team'
    # PASSWORD = os.environ['PASSWORD']

    BOLD_TEXT = '<strong>​​​​​​​hello</strong><br>'

    def test(self):
        login_and_write(self.driver, self.USEREMAIL, self.PASSWORD)

        # форматирование письма
        letter_formatting_page = LetterFormattingPage(self.driver)
        letter_formatting_form = letter_formatting_page.form
        letter_formatting_form.open_writing_letter()
        letter_formatting_form.click_on_bold_icon()
        letter_formatting_form.write_some_text("hello")
        # letter_formatting_form.text_selection()
        bold_text = letter_formatting_form.get_text()
        self.assertEqual(self.BOLD_TEXT.decode('utf-8'), bold_text)
