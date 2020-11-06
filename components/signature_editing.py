# -*- coding: utf-8 -*-
from base import Component

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignatureEditingForm(Component):

    POPUP0 = '//div[@data-test-id="signature-edit:0-popup"]'
    POPUP1 = '//div[@data-test-id="signature-edit:1-popup"]'
    POPUP2 = '//div[@data-test-id="signature-edit:2-popup"]'

    CANCEL0 = POPUP0 + '//button[@data-test-id="cancel"]'
    CANCEL1 = POPUP1 + '//button[@data-test-id="cancel"]'
    CANCEL2 = POPUP2 + '//button[@data-test-id="cancel"]'

    SAVE0 = POPUP0 + '//button[@data-test-id="save"]'
    SAVE1 = POPUP1 + '//button[@data-test-id="save"]'
    SAVE2 = POPUP2 + '//button[@data-test-id="save"]'

    SENDER_NAME0 = POPUP0 + '//input[@data-test-id="name_input"]'
    SENDER_NAME1 = POPUP1 + '//input[@data-test-id="name_input"]'
    SENDER_NAME2 = POPUP2 + '//input[@data-test-id="name_input"]'

    AS_DEFAULT0 = POPUP0 + '//label[@data-test-id="active-disabled"]'
    AS_DEFAULT1 = POPUP1 + '//label[@data-test-id="active-disabled"]'
    AS_DEFAULT2 = POPUP2 + '//label[@data-test-id="active-disabled"]'

    WARNING0 = POPUP0 + '//div[@data-test-id="error-footer-text"]'
    WARNING1 = POPUP1 + '//div[@data-test-id="error-footer-text"]'
    WARNING2 = POPUP2 + '//div[@data-test-id="error-footer-text"]'

    CROSS0 = POPUP0 + '//div[@data-test-id="cross"]'
    CROSS1 = POPUP1 + '//div[@data-test-id="cross"]'
    CROSS2 = POPUP2 + '//div[@data-test-id="cross"]'

    def set_first_sender_name(self, name):
        """
        Устанавливает имя отправителя в окне редактирования первой подписи
        :param name: имя отправителя
        """
        s_name = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SENDER_NAME0)
        )
        s_name.send_keys(name)

    def set_second_sender_name(self, name):
        """
        Устанавливает имя отправителя в окне редактирования второй подписи
        :param name: имя отправителя
        """
        s_name = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SENDER_NAME1)
        )
        s_name.send_keys(name)

    def set_third_sender_name(self, name):
        """
        Устанавливает имя отправителя в окне редактирования третьей подписи
        :param name: имя отправителя
        """
        s_name = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SENDER_NAME2)
        )
        s_name.send_keys(name)

    def clear_first_sender_name(self):
        """
        Очищает имя отправителя в окне редактирования первой подписи
        """
        s_name = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SENDER_NAME0)
        )
        s_name.clear()

    def clear_second_sender_name(self):
        """
        Очищает имя отправителя в окне редактирования второй подписи
        """
        s_name = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SENDER_NAME1)
        )
        s_name.clear()

    def clear_third_sender_name(self):
        """
        Очищает имя отправителя в окне редактирования третьей подписи
        """
        s_name = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SENDER_NAME2)
        )
        s_name.clear()

    def save_first(self):
        """
        Нажимает на кнопку сохранения изменений первой подписи
        """
        save = WebDriverWait(self.driver, 5, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE0))
        )
        save.click()

    def save_second(self):
        """
        Нажимает на кнопку сохранения изменений второй подписи
        """
        save = WebDriverWait(self.driver, 5, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE1))
        )
        save.click()

    def save_third(self):
        """
        Нажимает на кнопку сохранения изменений третьей подписи
        """
        save = WebDriverWait(self.driver, 5, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE2))
        )
        save.click()

    def mark_first_as_default(self):
        """
        Помечает первую подпись по умолчанию
        """
        as_default = WebDriverWait(self.driver, 5, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.AS_DEFAULT0))
        )
        as_default.click()

    def mark_second_as_default(self):
        """
        Помечает вторую подпись по умолчанию
        """
        as_default = WebDriverWait(self.driver, 5, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.AS_DEFAULT1))
        )
        as_default.click()

    def mark_third_as_default(self):
        """
        Помечает третью подпись по умолчанию
        """
        as_default = WebDriverWait(self.driver, 5, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.AS_DEFAULT2))
        )
        as_default.click()

    def first_empty_warning_appeared(self):
        """
        Проверяет, появилось ли сообщение о пустом вводе имени отпраивтеля у первой подписи
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING0)
            return True
        except NoSuchElementException:
            return False

    def second_empty_warning_appeared(self):
        """
        Проверяет, появилось ли сообщение о пустом вводе имени отпраивтеля у второй подписи
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING1)
            return True
        except NoSuchElementException:
            return False

    def third_empty_warning_appeared(self):
        """
        Проверяет, появилось ли сообщение о пустом вводе имени отпраивтеля у третьей подписи
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING2)
            return True
        except NoSuchElementException:
            return False

    def first_forbidden_warning_appeared(self):
        """
        Проверяет, появилось ли сообщение о некорректных символах в имени отпраивтеля у первой подписи
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING0)
            return True
        except NoSuchElementException:
            return False

    def second_forbidden_warning_appeared(self):
        """
        Проверяет, появилось ли сообщение о некорректных символах в имени отпраивтеля у второй подписи
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING1)
            return True
        except NoSuchElementException:
            return False

    def third_forbidden_warning_appeared(self):
        """
        Проверяет, появилось ли сообщение о некорректных символах в имени отпраивтеля у третьей подписи
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING2)
            return True
        except NoSuchElementException:
            return False

    def first_too_long_warning_appeared(self):
        """
        Проверяет, появилось ли сообщение о слишком длинном имени отпраивтеля у первой подписи
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING0)
            return True
        except NoSuchElementException:
            return False

    def second_too_long_warning_appeared(self):
        """
        Проверяет, появилось ли сообщение о слишком длинном имени отпраивтеля у второй подписи
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING1)
            return True
        except NoSuchElementException:
            return False

    def third_too_long_warning_appeared(self):
        """
        Проверяет, появилось ли сообщение о слишком длинном имени отпраивтеля у третьей подписи
        """
        try:
            self.driver.find_element_by_xpath(self.WARNING2)
            return True
        except NoSuchElementException:
            return False

    def abort_first(self):
        """
        Нажимает на кнопку отмены изменения первой подписи
        """
        self.driver.find_element_by_xpath(self.CANCEL0).click()

    def abort_second(self):
        """
        Нажимает на кнопку отмены изменения второй подписи
        """
        self.driver.find_element_by_xpath(self.CANCEL1).click()

    def abort_third(self):
        """
        Нажимает на кнопку отмены изменения третьей подписи
        """
        self.driver.find_element_by_xpath(self.CANCEL2).click()

    def is_first_hidden(self):
        """
        Проверяет, скрыто ли окно редактирования первой подписи
        """
        try:
            b = WebDriverWait(self.driver, 5, 0.1).until_not(
                lambda d: d.find_element_by_xpath(self.POPUP0)
            )
            return True
        except NoSuchElementException:
            return False

    def is_second_hidden(self):
        """
        Проверяет, скрыто ли окно редактирования второй подписи
        """
        try:
            b = WebDriverWait(self.driver, 5, 0.1).until_not(
                lambda d: d.find_element_by_xpath(self.POPUP1)
            )
            return True
        except NoSuchElementException:
            return False

    def is_third_hidden(self):
        """
        Проверяет, открыто ли окно редактирования третьей подписи
        """
        try:
            b = WebDriverWait(self.driver, 5, 0.1).until_not(
                lambda d: d.find_element_by_xpath(self.POPUP2)
            )
            return True
        except NoSuchElementException:
            return False

    def is_first_open(self):
        """
        Проверяет, открыто ли окно редактирования первой подписи
        """
        try:
            b = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.POPUP0)
            )
            return True
        except NoSuchElementException:
            return False

    def is_second_open(self):
        """
        Проверяет, открыто ли окно редактирования второй подписи
        """
        try:
            b = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.POPUP0)
            )
            return True
        except NoSuchElementException:
            return False

    def is_third_open(self):
        """
        Проверяет, открыто ли окно редактирования третьей подписи
        """
        try:
            b = WebDriverWait(self.driver, 5, 0.1).until(
                lambda d: d.find_element_by_xpath(self.POPUP0)
            )
            return True
        except NoSuchElementException:
            return False

    def close_first(self):
        """
        Нажимает на крестик у первой подписи
        """
        close = WebDriverWait(self.driver, 5, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.CROSS0))
        )
        close.click()

    def close_second(self):
        """
        Нажимает на крестик у второй подписи
        """
        close = WebDriverWait(self.driver, 5, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.CROSS1))
        )
        close.click()

    def close_third(self):
        """
        Нажимает на крестик у третьей подписи
        """
        close = WebDriverWait(self.driver, 5, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.CROSS2))
        )
        close.click()