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

    # Редактор

    EDITOR_TOOLBAR0 = POPUP0 + '//div[@data-test-id="editor"]'
    EDITOR_TOOLBAR_TOOL_BOLD0 = '//div[@data-test-id="bold"]'
    EDITOR_TOOLBAR_TOOL_BOLD_ACTIVE0 = '//div[@data-test-id="bold:active"]'

    EDITOR_TOOLBAR_TOOL_ITALIC0 = '//div[@data-test-id="italic"]'
    EDITOR_TOOLBAR_TOOL_ITALIC_ACTIVE0 = '//div[@data-test-id="italic:active"]'

    EDITOR_TOOLBAR_TOOL_UNDERLINE0 = '//div[@data-test-id="underline"]'
    EDITOR_TOOLBAR_TOOL_UNDERLINE_ACTIVE0 = '//div[@data-test-id="underline:active"]'

    EDITOR_TOOLBAR_TOOL_UNDO0 = '//div[@data-test-id="undo"]'
    EDITOR_TOOLBAR_TOOL_REDO0 = '//div[@data-test-id="redo"]'
    EDITOR_TOOLBAR_TOOL_LINK0 = '//div[@data-test-id="link"]'
    EDITOR_TOOLBAR_TOOL_INLINE_INPUT0 = '//div[@data-test-id="inline-input"]/button[@type="button"]/input[@type="file"]'
    EDITOR_TOOLBAR_TOOL_UNFORMAT0 = '//div[@data-test-id="unformat"]'

    EDITOR_TOOLBAR_TOOL_ALIGN0 = '//div[@data-test-id="align"]'

    EDITOR_TOOLBAR_TOOL_ALIGN_LEFT = '//div[@data-test-id="left"]'
    EDITOR_TOOLBAR_TOOL_ALIGN_RIGHT = '//div[@data-test-id="right"]'
    EDITOR_TOOLBAR_TOOL_ALIGN_CENTER = '//div[@data-test-id="center"]'

    EDITOR_TOOLBAR_TOOL_ALIGN_LEFT_ACTIVE = '//span[@data-test-id="left:active"]'
    EDITOR_TOOLBAR_TOOL_ALIGN_RIGHT_ACTIVE = '//span[@data-test-id="right:active"]'
    EDITOR_TOOLBAR_TOOL_ALIGN_CENTER_ACTIVE = '//span[@data-test-id="center:active"]'

    EDITOR_TOOLBAR_TOOL_INDENT_INCREASE = '//div[@data-test-id="right"]'
    EDITOR_TOOLBAR_TOOL_INDENT_DECREASE = '//div[@data-test-id="decrease"]'

    EDITOR_TOOLBAR_TOOL_STYLE_TAB = '//span[@data-test-id="right"]'
    EDITOR_TOOLBAR_TOOL_FONT_TAB = '//span[@data-test-id="decrease"]'

    EDITOR_TOOLBAR_TOOL_INDENT0 = '//div[@data-test-id="indent"]'

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
        undo_button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_ITALIC0)
        )
        try:
            # Проверка на :active
            undo_button.click()
            return True
        except:
            return False

    def check_is_active_italic(self):
        """
        Проверка нажатия на italic
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
            # Проверка на откат всего
            button.click()
            return True
        except:
            return False

    def set_big_signature_text(self, text):
        """
        Проверка на ошибку с большим текстом
        """
        #todo найти куда пихать текст на дохуя символов
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_UNFORMAT0)
        )
        try:
            #todo проверка на наличие текста внизу
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
        Проверка клика на undo
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
        Проверка клика на undo
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
        Проверка клика на undo
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
        Проверка клика на undo
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
        Проверка клика на undo
        """
        button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_INDENT0)
        )
        try:
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
        Проверка клика на increase
        """
        try:
            button = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_INDENT_DECREASE)
            )
            button.click()
            return True
        except:
            return False

    def click_fonts(self):
        """
        Проверка клика на increase
        """
        try:
            button = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.EDITOR_TOOLBAR_TOOL_INDENT_DECREASE)
            )
            button.click()
            return True
        except:
            return False
