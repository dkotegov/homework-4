# -*- coding: utf-8 -*-

import unittest

from pages.settings_page import SettingsPage
from setup.default_setup import default_setup

import os
import time


class DeepEditingTest(unittest.TestCase):
    NORMAL0_STRING = 'Sergei Petrenko'
    NORMAL1_STRING = u'Сергей Петренко'

    UNICODE_STRING = u'åΩ!2#%_=+±§'  # эмодзи не поддерживаются селениумом, инжектить js – геморройно
    EMPTY_STRING = ''
    SPACE_STRING = ' '

    FORBIDDEN_STRING = '<>:"'

    TOO_LONG_STRING = 'x' * 101

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
        assert editing.upload_inline_input_no_image_error_check(os.getcwd() + "/files/README.md")
        assert editing.upload_inline_input_no_image_error_check(os.getcwd() + "/files/fail.png")
        assert not editing.upload_inline_input_no_image_error_check(os.getcwd() + "/files/indus.jpeg")

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

    def test_toolbar_buttons_onclick_undo(self):
        """
           Проверки нажатия на кнопку redo
        """
        editing = self.settings.deep_editing()
        assert editing.click_bold()
        assert editing.check_is_active_bold()

        assert editing.click_undo()
        assert not editing.check_is_active_bold()

    def test_toolbar_buttons_onclick_redo(self):
        """
           Проверки нажатия на кнопку undo
        """
        editing = self.settings.deep_editing()
        assert editing.click_bold()
        assert editing.check_is_active_bold()

        assert editing.click_undo()
        assert not editing.check_is_active_bold()

        assert editing.click_redo()
        assert editing.check_is_active_bold()

    def test_toolbar_buttons_onclick_align_center(self):
        """
           Проверки нажатия на кнопку align с выравниваением по центру
        """
        editing = self.settings.deep_editing()
        assert editing.click_align()
        time.sleep(2)
        assert editing.check_align_data_list_button_center()
        time.sleep(2)
        assert editing.click_align()
        time.sleep(2)
        assert editing.check_align_data_list_button_center_active()
        time.sleep(2)

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
           Проверки нажатия на кнопку indent с increase
        """
        editing = self.settings.deep_editing()
        assert editing.click_indent()
        assert editing.check_indent_decrease()



    # def test_toolbar_buttons(self):
    #     """
    #     Переход кнопок в активное состояние
    #
    #     Замутить пару массивов кнопок
    #     Протыкать маассив
    #     Прочекать активность
    #     Нажать н раз редо
    #
    #     Проверить откат
    #
    #     Нажать н раз ундо
    #
    #     Проверить откат
    #     """
    #     editing = self.settings.deep_editing()
    #
    # def test_big_signature(self):
    #     """
    #     Охренеть какая длинная подпись на 10240 символов
    #     """
    #     editing = self.settings.deep_editing()
    #

