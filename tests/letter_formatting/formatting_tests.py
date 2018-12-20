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


class NumberedListTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # проверка списка
        # нумерованный список
        self.letter_formatting_form.click_on_list_icon()
        self.letter_formatting_form.click_on_numbered_list()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        numberred_list = self.letter_formatting_form.get_numbered_text()
        self.assertEqual(self.LISTED_TEXT.decode('utf-8'), numberred_list)


class MarkedListTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # маркированный список
        self.letter_formatting_form.click_on_list_icon()
        self.letter_formatting_form.click_on_bulleted_list()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        bulleted_list = self.letter_formatting_form.get_bulleted_text()
        self.assertEqual(self.LISTED_TEXT.decode('utf-8'), bulleted_list)


class CancelButtonTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # проверка работы кнопки отменить
        self.letter_formatting_form.click_on_list_icon()
        self.letter_formatting_form.click_on_numbered_list()
        # letter_formatting_form.click_on_message_field()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        numberred_list = self.letter_formatting_form.get_numbered_text()

        self.letter_formatting_form.click_on_repeat_icon()
        self.letter_formatting_form.click_on_repeat_icon()
        self.assertEqual(self.LISTED_TEXT.decode('utf-8'), numberred_list)


class LinkInsertionTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # проверка вствки ссылки
        self.letter_formatting_form.click_on_link_icon()
        self.letter_formatting_form.write_some_text(self.LINK)
        self.letter_formatting_form.click_on_tab_key()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        self.letter_formatting_form.click_on_ok_link_button()
        href, linked_text = self.letter_formatting_form.get_link()
        self.assertEqual(self.SAMPLE_TEXT, linked_text)
        self.assertEqual(self.LINK.decode('utf-8'), href)


class ImageInsertTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # проверка вставки картинки
        self.letter_formatting_form.send_picture()
        img = self.letter_formatting_form.get_img()
        self.assertIn('<img', img)


class ClearFormatingTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # проверка очистки форматирования
        self.letter_formatting_form.click_on_bold_icon()
        self.letter_formatting_form.click_on_clear_formatting_icon()
        self.letter_formatting_form.click_on_message_field()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        text = self.letter_formatting_form.get_text()
        self.assertIn(self.NOT_BOLD_TEXT.decode('utf-8'), text)
