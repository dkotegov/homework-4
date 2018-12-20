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


class UnderlinedTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)

        # очистка поля ввода сообещния
        self.letter_formatting_form.clear_field()

        # проверка подчёркнутого текста
        self.letter_formatting_form.click_on_underlined_icon()
        self.letter_formatting_form.click_on_message_field()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        underlined_text = self.letter_formatting_form.get_text()
        self.assertEqual(self.UNDERLINED_TEXT.decode('utf-8'), underlined_text)


class StrikeThroughTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # очистка поля ввода сообещния
        self.letter_formatting_form.clear_field()
        # проверка зачёркнутого текста
        self.letter_formatting_form.click_on_strikethrough_icon()
        self.letter_formatting_form.click_on_message_field()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        strikethrough_text = self.letter_formatting_form.get_text()
        self.assertEqual(self.STRIKETHROUGH_TEXT.decode('utf-8'), strikethrough_text)


class ColorTextTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # очистка поля ввода сообещния
        self.letter_formatting_form.clear_field()
        # проверка цвета текста
        self.letter_formatting_form.click_on_color_text_icon()
        self.letter_formatting_form.click_on_color_value()
        self.letter_formatting_form.click_on_message_field()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        color_value = self.letter_formatting_form.get_text_color()
        self.assertEqual(self.TEXT_COLOR, color_value)


class BackgroundColorTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # очистка поля ввода сообещния
        self.letter_formatting_form.clear_field()
        # проверка цвета фона
        self.letter_formatting_form.click_on_background_color_icon()
        self.letter_formatting_form.click_on_background_color_value()
        self.letter_formatting_form.click_on_message_field()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        color_value = self.letter_formatting_form.get_background_color()
        self.assertEqual(self.TEXT_COLOR, color_value)


class FontIconTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # очистка поля ввода сообещния
        self.letter_formatting_form.clear_field()
        # проверка шрифта
        self.letter_formatting_form.click_on_font_icon()
        self.letter_formatting_form.click_on_font_value()
        self.letter_formatting_form.click_on_message_field()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        size_of_text = self.letter_formatting_form.get_size_of_text()
        line_height_of_text = self.letter_formatting_form.get_line_height_of_text()
        self.assertEqual(self.FONT_SIZE, size_of_text)
        self.assertEqual(self.LINE_HEIGHT, line_height_of_text)


class TextAlignTest(BaseFormatting):
    def test(self):
        BaseFormatting.test(self)
        # очистка поля ввода сообещния
        self.letter_formatting_form.clear_field()

        # проверка выравнивания текста
        self.letter_formatting_form.click_on_text_align_icon()
        self.letter_formatting_form.click_on_text_align_value_icon()
        # letter_formatting_form.click_on_message_field()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        # letter_formatting_form.text_selection()
        align_of_text = self.letter_formatting_form.get_align_of_text()
        self.assertEqual(self.TEXT_ALIGN, align_of_text)


class MarginIconTest(BaseFormatting):

    def test(self):
        BaseFormatting.test(self)
        # очистка поля ввода сообещния
        self.letter_formatting_form.clear_field()
        # проверка отступа текста
        # увеличение отступа
        self.letter_formatting_form.click_on_text_margin_icon()
        self.letter_formatting_form.click_on_text_margin_inc()
        self.letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        margin_of_text = self.letter_formatting_form.get_margin_of_text()
        self.assertEqual(self.MARGIN_LEFT, margin_of_text)
        # уменьшение отступа
        self.letter_formatting_form.click_on_text_margin_icon()
        self.letter_formatting_form.click_on_text_margin_dec()
        margin_of_text = self.letter_formatting_form.get_margin_of_text()
        self.assertEqual('0px', margin_of_text)


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
