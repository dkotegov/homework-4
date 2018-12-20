# coding=utf-8
from pages.letter_formatting_page import LetterFormattingPage
from tests.letter_formatting.base_formatting import BaseFormatting


class BoldTest(BaseFormatting):

    def test(self):
        BaseFormatting.test(self)

        # очистка поля ввода сообещния
        self.letter_formatting_form.clear_field()
        # проверка жирного шрифта
        self.letter_formatting_form.click_on_bold_icon()
        self.letter_formatting_form.click_on_message_field()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        bold_text = self.letter_formatting_form.get_text()
        self.assertEqual(self.BOLD_TEXT.decode('utf-8'), bold_text)


class ItalicTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # очистка поля ввода сообещния
        self.letter_formatting_form.clear_field()

        # проверка курсивного шрифта
        self.letter_formatting_form.click_on_italic_icon()
        # letter_formatting_form.click_on_message_field()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        italic_text = self.letter_formatting_form.get_text()
        self.assertEqual(self.ITALIC_TEXT.decode('utf-8'), italic_text)
