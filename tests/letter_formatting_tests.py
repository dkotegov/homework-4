# coding=utf-8
import os
import unittest

from components.login_and_write import login_and_write
from pages.letter_formatting_page import LetterFormattingPage
from tests.base_test import BaseTest


class LetterFormattingTests(BaseTest):
    SAMPLE_TEXT = 'hello'
    BOLD_TEXT = '<strong>​​​​​​​' + SAMPLE_TEXT + '</strong><br>'
    ITALIC_TEXT = '<em>​​​​​​​' + SAMPLE_TEXT + '</em><br>'
    UNDERLINED_TEXT = '<u>​​​​​​​' + SAMPLE_TEXT + '</u><br>'
    STRIKETHROUGH_TEXT = '<s>​​​​​​​' + SAMPLE_TEXT + '</s><br>'
    TEXT_COLOR = 'rgba(202, 242, 245, 1)'
    FONT_SIZE = '32px'
    LINE_HEIGHT = '40px'
    TEXT_ALIGN = 'right'
    MARGIN_LEFT = '40px'

    def test(self):
        login_and_write(self.driver, self.USEREMAIL, self.PASSWORD)

        letter_formatting_page = LetterFormattingPage(self.driver)
        letter_formatting_form = letter_formatting_page.form
        letter_formatting_form.open_writing_letter()

        # проверка жирного шрифта
        letter_formatting_form.click_on_bold_icon()
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        # letter_formatting_form.text_selection()
        bold_text = letter_formatting_form.get_text()
        self.assertEqual(self.BOLD_TEXT.decode('utf-8'), bold_text)

        # очистка поля ввода сообещния
        letter_formatting_form.clear_field()

        # проверка курсивного шрифта
        letter_formatting_form.click_on_italic_icon()
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        italic_text = letter_formatting_form.get_text()
        self.assertEqual(self.ITALIC_TEXT.decode('utf-8'), italic_text)

        # очистка поля ввода сообещния
        letter_formatting_form.clear_field()

        # проверка подчёркнутого текста
        letter_formatting_form.click_on_underlined_icon()
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        underlined_text = letter_formatting_form.get_text()
        self.assertEqual(self.UNDERLINED_TEXT.decode('utf-8'), underlined_text)

        # очистка поля ввода сообещния
        letter_formatting_form.clear_field()

        # проверка зачёркнутого текста
        letter_formatting_form.click_on_strikethrough_icon()
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        strikethrough_text = letter_formatting_form.get_text()
        self.assertEqual(self.STRIKETHROUGH_TEXT.decode('utf-8'), strikethrough_text)

        # очистка поля ввода сообещния
        letter_formatting_form.clear_field()

        # проверка цвета текста
        letter_formatting_form.click_on_color_text_icon()
        letter_formatting_form.click_on_color_value()
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        color_value = letter_formatting_form.get_text_color()
        self.assertEqual(self.TEXT_COLOR, color_value)

        # очистка поля ввода сообещния
        letter_formatting_form.clear_field()

        # проверка цвета фона
        letter_formatting_form.click_on_background_color_icon()
        letter_formatting_form.click_on_background_color_value()
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        color_value = letter_formatting_form.get_background_color()
        self.assertEqual(self.TEXT_COLOR, color_value)

        # очистка поля ввода сообещния
        letter_formatting_form.clear_field()

        # проверка шрифта
        letter_formatting_form.click_on_font_icon()
        letter_formatting_form.click_on_font_value()
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        size_of_text = letter_formatting_form.get_size_of_text()
        line_height_of_text = letter_formatting_form.get_line_height_of_text()
        self.assertEqual(self.FONT_SIZE, size_of_text)
        self.assertEqual(self.LINE_HEIGHT, line_height_of_text)

        # очистка поля ввода сообещния
        letter_formatting_form.clear_field()

        # проверка выравнивания текста
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        letter_formatting_form.text_selection()
        letter_formatting_form.click_on_text_align_icon()
        letter_formatting_form.click_on_text_align_value_icon()
        align_of_text = letter_formatting_form.get_align_of_text()
        self.assertEqual(self.TEXT_ALIGN, align_of_text)

        # очистка поля ввода сообещния
        letter_formatting_form.full_clear_field()

        # проверка отступа текста
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        letter_formatting_form.text_selection()
        letter_formatting_form.click_on_text_margin_icon()
        letter_formatting_form.click_on_text_margin_value_icon()
        margin_of_text = letter_formatting_form.get_margin_of_text()
        self.assertEqual(self.MARGIN_LEFT, margin_of_text)
