# -*- coding: utf-8 -*-
from base import Component

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignatureCreationForm(Component):

    POPUP = '//div[@data-test-id="signature-create-popup"]'

    CANCEL = POPUP + '//button[@data-test-id="cancel"]'
    SAVE = POPUP + '//button[@data-test-id="save"]'

    SENDER_NAME = POPUP + '//input[@data-test-id="name_input"]'

    AS_DEFAULT = POPUP + '//label[@data-test-id="active-disabled"]'

    WARNING = POPUP + '//div[@data-test-id="error-footer-text"]'

    CROSS = '//div[@data-test-id="cross"]'

    def set_sender_name(self, name):
        """
        Вводит имя отправителя (Не очищает раннее введенные данные)
        :param name: имя отправителя
        """
        s_name = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SENDER_NAME)
        )
        s_name.send_keys(name)

    def clear_sender_name(self):
        """
        Очищает поле "имя отправителя"
        """
        s_name = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SENDER_NAME)
        )
        s_name.clear()

    def create(self):
        """
        Нажимает на кнопку создания подписи
        """
        save = WebDriverWait(self.driver, 5, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE))
        )
        save.click()

    def mark_as_default(self):
        """
        Помечает подпись по умолчанию
        """
        as_default = WebDriverWait(self.driver, 5, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.AS_DEFAULT))
        )
        as_default.click()

    def empty_warning_appeared(self):
        """
        Проверяет, есть ли уведомление о пустом вводе
        :return: True, False
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING)
            return True
        except NoSuchElementException:
            return False

    def forbidden_warning_appeared(self):
        """
        Проверяет, есть ли уведомление о запрещенных символах
        :return: True, False
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING)
            return True
        except NoSuchElementException:
            return False

    def too_long_warning_appeared(self):
        """
        Проверяет, есть ли уведомление о слишком длинном имени
        :return: True, False
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING)
            return True
        except NoSuchElementException:
            return False

    def abort(self):
        """
        Нажимает на кнопку отмены создания
        """
        self.driver.find_element_by_xpath(self.CANCEL).click()

    def is_hidden(self):
        """
        Проверяет, скрыто ли окно создания
        :return: True, False
        """
        try:
            b = WebDriverWait(self.driver, 5, 0.1).until_not(
                lambda d: d.find_element_by_xpath(self.POPUP)
            )
            return True
        except NoSuchElementException:
            return False

    def is_open(self):
        """
        Проверяет, открыто ли окно создания
        :return: True, False
        """
        try:
            b = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.POPUP)
            )
            return True
        except NoSuchElementException:
            return False

    def close(self):
        """
        Нажимает на кнопку крестика
        """
        self.driver.find_element_by_xpath(self.CROSS).click()