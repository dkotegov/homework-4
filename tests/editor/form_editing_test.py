# -*- coding: utf-8 -*-

import unittest

from pages.settings_page import SettingsPage
from setup.default_setup import default_setup

import os
import time


class FormEditingTest(unittest.TestCase):
    NORMAL0_STRING = 'Sergei Petrenko'
    NORMAL1_STRING = u'Сергей Петренко'
    TOO_LONG_STRING = 'x' * 10250
    README_PATH = os.getcwd() + "/files/README.md"
    FAIL_PATH = os.getcwd() + "/files/fail.png"
    CORRECT_PATH = os.getcwd() + "/files/indus.jpeg"

    def setUp(self):
        default_setup(self)

        self.settings = SettingsPage(self.driver)
        self.settings.open()
        self.settings.clear_signatures()

        general = self.settings.general()
        general.create_signature()

    def tearDown(self):
        self.driver.quit()

    def test_editing_file_input(self):
        """
        Загрузка файлов
        """
        editing = self.settings.deep_editing()
        assert editing.upload_inline_input_no_image_error_check(self.README_PATH)
        assert editing.upload_inline_input_no_image_error_check(self.FAIL_PATH)
        assert not editing.upload_inline_input_no_image_error_check(self.CORRECT_PATH)

    def test_toolbar_buttons_onclick_bold(self):
        """
           Проверки нажатия на кнопку bold
        """
        editing = self.settings.deep_editing()
        assert editing.click_bold()
        assert editing.check_is_active_bold()

    def test_toolbar_buttons_onclick_italic(self):
        """
           Проверки нажатия на кнопку italic
        """
        editing = self.settings.deep_editing()
        assert editing.click_italic()
        assert editing.check_is_active_italic()

    # Проверки отмены/возврата действий

    def test_toolbar_buttons_onclick_undo(self):
        """
           Проверки нажатия на кнопку undo
        """
        editing = self.settings.deep_editing()
        assert editing.click_bold()
        assert editing.check_is_active_bold()

        assert editing.click_undo()
        assert not editing.check_is_active_bold()

    def test_toolbar_buttons_onclick_redo(self):
        """
           Проверки нажатия на кнопку redo
        """
        editing = self.settings.deep_editing()
        assert editing.click_bold()
        assert editing.check_is_active_bold()

        assert editing.click_undo()
        assert not editing.check_is_active_bold()

        assert editing.click_redo()
        assert editing.check_is_active_bold()

    # Проверки выравнивания текста

    def test_toolbar_buttons_onclick_align_center(self):
        """
           Проверки нажатия на кнопку align с выравниваением по центру
        """
        editing = self.settings.deep_editing()
        assert editing.click_align()
        assert editing.check_align_data_list_button_center()
        assert editing.click_align()
        assert editing.check_align_data_list_button_center_active()

    def test_toolbar_buttons_onclick_align_left(self):
        """
           Проверки нажатия на кнопку align с выравниваением по центру
        """
        editing = self.settings.deep_editing()
        assert editing.click_align()
        if not editing.check_align_data_list_button_left_active():
            assert editing.check_align_data_list_button_left()
            assert editing.click_align()

        assert editing.check_align_data_list_button_left_active()

    def test_toolbar_buttons_onclick_align_right(self):
        """
           Проверки нажатия на кнопку align с выравниваением по центру
        """
        editing = self.settings.deep_editing()
        assert editing.click_align()
        assert editing.check_align_data_list_button_right()
        assert editing.click_align()
        assert editing.check_align_data_list_button_right_active()

    def test_toolbar_buttons_onclick_indent_increase(self):
        """
           Проверки нажатия на кнопку indent с increase
        """
        editing = self.settings.deep_editing()
        assert editing.click_indent()
        assert editing.check_indent_increase()

    def test_toolbar_buttons_onclick_indent_decrease(self):
        """
           Проверки нажатия на кнопку indent с decrease
        """
        editing = self.settings.deep_editing()
        assert editing.click_indent()
        assert editing.check_indent_decrease()

    # Проверки изменения типа и стиля у текста

    def test_toolbar_buttons_onclick_font_style_tab(self):
        """
           Проверки нажатия на кнопку font с выбором стиля
        """
        editing = self.settings.deep_editing()
        assert editing.click_font()
        assert editing.click_tab_style()

    def test_toolbar_buttons_onclick_font_font_tab(self):
        """
           Проверки нажатия на кнопку font с выбором шрифта
        """
        editing = self.settings.deep_editing()
        assert editing.click_font()
        assert editing.click_tab_font()

    def test_toolbar_select_font(self):
        """
           Проверки выбора типа шрифта
        """
        editing = self.settings.deep_editing()
        assert editing.click_font()
        assert editing.click_tab_font()
        assert editing.click_tab_font_helvetica()

    def test_toolbar_select_style(self):
        """
           Проверки выбора стиля шрифта
        """
        editing = self.settings.deep_editing()
        assert editing.click_font()
        assert editing.click_tab_style()
        assert editing.click_tab_style_normal()

    # Проверки изменения цвета и фона у текста

    def test_toolbar_buttons_onclick_color_color_tab(self):
        """
           Проверки нажатия на кнопку font с выбором стиля
        """
        editing = self.settings.deep_editing()
        assert editing.click_button_color()
        assert editing.click_button_color_tab_color()

    def test_toolbar_buttons_onclick_color_background_tab(self):
        """
           Проверки нажатия на кнопку font с выбором шрифта
        """
        editing = self.settings.deep_editing()
        assert editing.click_button_color()
        assert editing.click_button_color_tab_background()

    # Добавление ссылок

    def test_toolbar_add_link(self):
        """
           Проверка добавления корректной ссылки
        """
        editing = self.settings.deep_editing()
        assert editing.click_button_link()
        assert editing.set_toolbar_link('http://test.ru')
        assert editing.set_toolbar_link_text('test')
        assert editing.click_toolbar_link_save()

    def test_toolbar_add_link_cancel(self):
        """
           Проверка отмены добавления ссылки
        """
        editing = self.settings.deep_editing()
        assert editing.click_button_link()
        assert editing.click_toolbar_link_cancel()

    def test_toolbar_add_link_check_warning(self):
        """
           Проверка добавления невалидной ссылки
        """
        editing = self.settings.deep_editing()
        assert editing.click_button_link()
        assert editing.set_toolbar_link('hppts://test.ru')
        assert not editing.toolbar_link_check_no_warning()
        assert editing.click_toolbar_link_cancel()



