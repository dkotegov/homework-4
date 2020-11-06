# -*- coding: utf-8 -*-
from base import Component

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time


class SignatureDeepEditingForm(Component):
    POPUP0 = '//div[@data-test-id="signature-edit:0-popup"]'
    POPUP1 = '//div[@data-test-id="signature-edit:1-popup"]'
    POPUP2 = '//div[@data-test-id="signature-edit:2-popup"]'

    CANCEL0 = POPUP0 + '//span[text()="Отменить"]'
    CANCEL1 = POPUP1 + '//span[text()="Отменить"]'
    CANCEL2 = POPUP2 + '//span[text()="Отменить"]'

    SAVE0 = POPUP0 + '//button[@data-test-id="save"]'
    SAVE1 = POPUP1 + '//button[@data-test-id="save"]'
    SAVE2 = POPUP2 + '//button[@data-test-id="save"]'

    SENDER_NAME0 = POPUP0 + '//input[@data-test-id="name_input"]'
    SENDER_NAME1 = POPUP1 + '//input[@data-test-id="name_input"]'
    SENDER_NAME2 = POPUP2 + '//input[@data-test-id="name_input"]'

    AS_DEFAULT0 = POPUP0 + '//label[@data-test-id="active-disabled"]'
    AS_DEFAULT1 = POPUP1 + '//label[@data-test-id="active-disabled"]'
    AS_DEFAULT2 = POPUP2 + '//label[@data-test-id="active-disabled"]'

    EMPTY_WARNING0 = POPUP0 + '//small[text()="Заполните обязательное поле"]'
    EMPTY_WARNING1 = POPUP1 + '//small[text()="Заполните обязательное поле"]'
    EMPTY_WARNING2 = POPUP2 + '//small[text()="Заполните обязательное поле"]'

    TOO_LONG_WARNING0 = POPUP0 + '//small[text()="Имя отправителя должно быть короче 100 символов"] '
    TOO_LONG_WARNING1 = POPUP1 + '//small[text()="Имя отправителя должно быть короче 100 символов"] '
    TOO_LONG_WARNING2 = POPUP2 + '//small[text()="Имя отправителя должно быть короче 100 символов"] '

    FORBIDDEN_WARNING0 = POPUP0 + '//small[starts-with(text(),"Имя отправителя")]'
    FORBIDDEN_WARNING1 = POPUP1 + '//small[starts-with(text(),"Имя отправителя")]'
    FORBIDDEN_WARNING2 = POPUP2 + '//small[starts-with(text(),"Имя отправителя")]'

    # Все для тулбара

    EDITOR_TOOLBAR0 = POPUP0 + '//div[@data-test-id="editor"]'
    EDITOR_TOOLBAR_TOOL_BOLD0 = '//div[@data-test-id="bold"]'
    EDITOR_TOOLBAR_TOOL_BOLD_ACTIVE0 = '//div[@data-test-id="bold:active"]'

    EDITOR_TOOLBAR_TOOL_ITALIC0 = '//div[@data-test-id="italic"]'
    EDITOR_TOOLBAR_TOOL_ITALIC_ACTIVE0 = '//div[@data-test-id="italic:active"]'

    EDITOR_TOOLBAR_TOOL_UNDERLINE0 = '//div[@data-test-id="underline"]'
    EDITOR_TOOLBAR_TOOL_UNDERLINE_ACTIVE0 = '//div[@data-test-id="underline:active"]'

    EDITOR_TOOLBAR_TOOL_FONT = '//div[@data-test-id="font"]'
    EDITOR_TOOLBAR_TOOL_COLOR = '//div[@data-test-id="color"]'

    EDITOR_TOOLBAR_TOOL_UNDO0 = '//div[@data-test-id="undo"]'
    EDITOR_TOOLBAR_TOOL_REDO0 = '//div[@data-test-id="redo"]'

    EDITOR_TOOLBAR_TOOL_LINK0 = '//div[@data-test-id="link"]'
    EDITOR_TOOLBAR_TOOL_INLINE_INPUT0 = '//div[@data-test-id="inline-input"]/button[@type="button"]/input[@type="file"]'

    EDITOR_TOOLBAR_TOOL_ALIGN0 = '//div[@data-test-id="align"]'

    EDITOR_TOOLBAR_TOOL_ALIGN_LEFT = '//div[@data-test-id="left"]'
    EDITOR_TOOLBAR_TOOL_ALIGN_RIGHT = '//div[@data-test-id="right"]'
    EDITOR_TOOLBAR_TOOL_ALIGN_CENTER = '//div[@data-test-id="center"]'

    EDITOR_TOOLBAR_TOOL_ALIGN_LEFT_ACTIVE = '//span[@data-test-id="left:active"]'
    EDITOR_TOOLBAR_TOOL_ALIGN_RIGHT_ACTIVE = '//span[@data-test-id="right:active"]'
    EDITOR_TOOLBAR_TOOL_ALIGN_CENTER_ACTIVE = '//span[@data-test-id="center:active"]'

    EDITOR_TOOLBAR_TOOL_INDENT0 = '//div[@data-test-id="indent"]'
    EDITOR_TOOLBAR_TOOL_INDENT_INCREASE = '//div[@data-test-id="increase"]'
    EDITOR_TOOLBAR_TOOL_INDENT_DECREASE = '//div[@data-test-id="decrease"]'

    EDITOR_TOOLBAR_TOOL_STYLE_TAB = '//span[@data-test-id="style-tab"]'
    EDITOR_TOOLBAR_TOOL_FONT_TAB = '//span[@data-test-id="font-tab"]'

    EDITOR_TOOLBAR_TOOL_FONT_HELVETICA = '//div[@data-test-id="Arial"]'
    EDITOR_TOOLBAR_TOOL_STYLE_NORMAL = '//div[@data-test-id="normal"]'

    EDITOR_TOOLBAR_TOOL_COLOR_TAB = '//span[@data-test-id="color-tab"]'
    EDITOR_TOOLBAR_TOOL_BACKGROUND_TAB = '//span[@data-test-id="bg-tab"]'

    EDITOR_TOOLBAR_TOOL_COLOR_EXAMPLE_TEXT = '//span[starts-with(text(),"Пример оформления текста")]'

    EDITOR_TOOLBAR_TOOL_ORANGE_COLOR = '//div[@data-test-id="rgb(243, 144, 29)"]'
    EDITOR_TOOLBAR_TOOL_PINK_COLOR = '//div[@data-test-id="rgb(255, 0, 255)"]'

    EDITOR_TOOLBAR_LINK_INPUT = '//input[@data-test-id="link"]'
    EDITOR_TOOLBAR_LINK_TEXT_INPUT = '//form[@data-test-id="link-editor"]//input[@data-test-id="text"]'

    EDITOR_TOOLBAR_LINK_SAVE = '//form[@data-test-id="link-editor"]//button[@data-test-id="save"]'
    EDITOR_TOOLBAR_LINK_CANCEL = '//form[@data-test-id="link-editor"]//button[@data-test-id="cancel"]'

    EDITOR_TOOLBAR_LINK_ERROR_MESSAGE_CONTAINER = '//div[@data-test-id="error-footer-text"]'

    # todo проверки форматирования
    EDITOR_TOOLBAR_TOOL_UNFORMAT0 = '//div[@data-test-id="unformat"]'

    EDITOR_TEXTAREA_FIELD = '//div[@role="textbox"]'
    EDITOR_ERROR_FOOTER_TEXT = '//div[@data-test-id="error-footer-text"]/small[starts-with(text(),"Подпись не должна ' \
                               'быть длиннее 10240 символов")] '

    def upload_inline_input_no_image_error_check(self, file):
        """
        Загружаем в едитор файл и проверяем ошибки
        :param file: файл
        """
        inline_input = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_INLINE_INPUT0)
        )
        inline_input.send_keys(file)
        try:
            WebDriverWait(self.driver, 5, 0.1).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            return True
        except:
            return False

    def test_toolbar_buttons(self, file):
        """
        Устанавливает имя отправителя в окне редактирования первой подписи
        :param file: файл
        """
        inline_input = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_INLINE_INPUT0)
        )
        inline_input.send_keys(file)
        try:
            WebDriverWait(self.driver, 5, 0.1).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            return True
        except:
            return False

    def test_redo(self):
        """
        Проверка клика на redo
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_REDO0)
        )
        try:
            button.click()
            return True
        except:
            return False

    def test_undo(self):
        """
        Проверка клика на undo
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_UNDO0)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_bold(self):
        """
        Проверка клика на bold
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_BOLD0)
        )
        try:
            button.click()
            return True
        except:
            return False

    def check_is_active_bold(self):
        """
        Проверка нажатия на bold
        """
        try:
            button = WebDriverWait(self.driver, 5, 0.1).until(
                EC.element_to_be_clickable((By.XPATH, self.EDITOR_TOOLBAR_TOOL_BOLD_ACTIVE0))
            )
            return True
        except:
            return False

    def click_italic(self):
        """
        Проверка клика на italic
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_ITALIC0)
        )
        try:
            button.click()
            return True
        except:
            return False

    def check_is_active_italic(self):
        """
        Проверка клика на italic
        """
        try:
            button = WebDriverWait(self.driver, 5, 0.1).until(
                EC.element_to_be_clickable((By.XPATH, self.EDITOR_TOOLBAR_TOOL_ITALIC_ACTIVE0))
            )
            return True
        except:
            return False

    def click_underline(self):
        """
        Проверка клика на underline
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_UNDERLINE0)
        )
        try:
            # Проверка на :active
            button.click()
            return True
        except:
            return False

    def check_is_active_underline(self):
        """
        Проверка нажатия на italic
        """
        try:
            button = WebDriverWait(self.driver, 5, 0.1).until(
                EC.element_to_be_clickable((By.XPATH, self.EDITOR_TOOLBAR_TOOL_UNDERLINE_ACTIVE0))
            )
            return True
        except:
            return False

    def click_unformat(self):
        """
        Проверка клика на unformat
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_UNFORMAT0)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_redo(self):
        """
        Проверка клика на redo
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_REDO0)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_undo(self):
        """
        Проверка клика на undo
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_UNDO0)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_align(self):
        """
        Клика на undo
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_ALIGN0)
        )
        try:
            button.click()
            return True
        except:
            return False

    def check_align_data_list_button_center(self):
        """
        Клик на отцентровку
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_ALIGN_CENTER)
        )
        try:
            button.click()
            return True
        except:
            return False

    def check_align_data_list_button_center_active(self):
        """
        Проверка клика на отцентровку
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_ALIGN_CENTER_ACTIVE)
        )
        try:
            button.click()
            return True
        except:
            return False

    def check_align_data_list_button_left(self):
        """
        Клика на левое выравнивание
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_ALIGN_LEFT)
        )
        try:
            button.click()
            return True
        except:
            return False

    def check_align_data_list_button_left_active(self):
        """
        Проверка клика на undo
        """
        try:
            button = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_ALIGN_LEFT_ACTIVE)
            )
            button.click()
            return True
        except:
            return False

    def check_align_data_list_button_right(self):
        """
        Проверка клика на undo
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_ALIGN_RIGHT)
        )
        try:
            button.click()
            return True
        except:
            return False

    def check_align_data_list_button_right_active(self):
        """
        Проверка клика на undo
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_ALIGN_RIGHT_ACTIVE)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_indent(self):
        """
        Проверка клика на indent
        """
        try:
            button = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_INDENT0)
            )
            button.click()
            return True
        except:
            return False

    def check_indent_increase(self):
        """
        Проверка клика на increase
        """
        try:
            button = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_INDENT_INCREASE)
            )
            button.click()
            return True
        except:
            return False

    def check_indent_decrease(self):
        """
        Клика на decrease
        """
        try:
            button = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_INDENT_DECREASE)
            )
            button.click()
            return True
        except:
            return False

    def click_font(self):
        """
        Проверка клика на font
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_FONT)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_tab_font(self):
        """
        Проверка клика на font
        """

        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_FONT_TAB)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_tab_font_helvetica(self):
        """
        Клика на шрифт helvetica
        """

        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_FONT_HELVETICA)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_tab_style(self):
        """
        Клик на font
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_STYLE_TAB)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_tab_style_normal(self):
        """
        Клик на стиль normal
        """

        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_STYLE_NORMAL)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_button_color(self):
        """
        Клика на color для перехода на табы
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_COLOR)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_button_color_tab_color(self):
        """
        Клика на таб цвета
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_COLOR_TAB)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_button_color_tab_background(self):
        """
        Клика на таб фона
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_BACKGROUND_TAB)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_color_tab_orange_color(self):
        """
        Клик на оранджевый цвет для текста
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_ORANGE_COLOR)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_color_tab_pink_color(self):
        """
         Клик на розовый цвет для фона
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_PINK_COLOR)
        )
        try:
            button.click()
            return True
        except:
            return False

    def get_color_of_text(self):
        """
        Проверка клика на фон
        """
        text = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_COLOR_EXAMPLE_TEXT)
        )
        return text.value_of_css_property('color')

    def get_color_of_background(self):
        """
        Проверка клика на фон
        """
        text = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_COLOR_EXAMPLE_TEXT)
        )
        return text.value_of_css_property('background-color')

    def click_button_link(self):
        """
           Проверка клика на link
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_LINK0)
        )
        try:
            button.click()
            return True
        except:
            return False

    def set_toolbar_link(self, text):
        """
        Ввод ссылки
        """
        try:
            link = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_LINK_INPUT)
            )
            link.send_keys(text)
            return True
        except:
            return False

    def set_toolbar_link_text(self, text):
        """
        Ввод текста ссылки
        """
        try:
            link = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_LINK_TEXT_INPUT)
            )
            link.send_keys(text)
            return True
        except:
            return False

    def click_toolbar_link_save(self):
        """
        Сохранение ссылки
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_LINK_SAVE)
        )
        try:
            button.click()
            return True
        except:
            return False

    def click_toolbar_link_cancel(self):
        """
        Отмена добавления ссылки
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_LINK_CANCEL)
        )
        try:
            button.click()
            return True
        except:
            return False

    def toolbar_link_check_no_warning(self):
        """
        Проверка наличия ворнинга о некорректной ссылке
        """
        try:
            warining = WebDriverWait(self.driver, 2, 0.1).until(
                lambda d: d.find_element_by_xpath(self.EDITOR_ERROR_FOOTER_TEXT)
            )
            return True
        except:
            return False

    def set_text_to_textarea(self, text):
        """
        Добавление текста в текстовый блок
        """
        try:
            textarea = WebDriverWait(self.driver, 2, 0.1).until(
                lambda d: d.find_element_by_xpath(self.EDITOR_TEXTAREA_FIELD)
            )
            textarea.send_keys(text)
            return True
        except:
            return False

    def save_signature(self):
        """
        Проверка сохранения
        """
        try:
            button = WebDriverWait(self.driver, 2, 0.1).until(
                lambda d: d.find_element_by_xpath(self.SAVE0)
            )
            button.click()
            return True
        except:
            return False
