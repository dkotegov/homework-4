# -*- coding: utf-8 -*-
from base import Component

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingsGeneralForm(Component):
    ADD = '//button[@data-test-id="create"]'
    
    CONTAINER0 = '//div[@data-test-id="signature:0"]'
    CONTAINER1 = '//div[@data-test-id="signature:1"]'
    CONTAINER2 = '//div[@data-test-id="signature:2"]'
    
    SETACTIVE0 = CONTAINER0 + '//div[@data-test-id="set-active"]'
    SETACTIVE1 = CONTAINER1 + '//div[@data-test-id="set-active"]'
    SETACTIVE2 = CONTAINER2 + '//div[@data-test-id="set-active"]'

    NAME0 = CONTAINER0 + '//p[@data-test-id="name"]'
    NAME1 = CONTAINER1 + '//p[@data-test-id="name"]'
    NAME2 = CONTAINER2 + '//p[@data-test-id="name"]'

    REMOVE0 = CONTAINER0 + '//button[@data-test-id="remove"]'
    REMOVE1 = CONTAINER1 + '//button[@data-test-id="remove"]'
    REMOVE2 = CONTAINER2 + '//button[@data-test-id="remove"]'

    DEFAULT0 = CONTAINER0 + '//p[@data-test-id="active"]'
    DEFAULT1 = CONTAINER1 + '//p[@data-test-id="active"]'
    DEFAULT2 = CONTAINER2 + '//p[@data-test-id="active"]'

    EDIT0 = CONTAINER0 + '//button[@data-test-id="edit"]'
    EDIT1 = CONTAINER1 + '//button[@data-test-id="edit"]'
    EDIT2 = CONTAINER2 + '//button[@data-test-id="edit"]'

    def create_signature(self):
        """
        Нажимает на кнопку создания подписи
        """
        add_button = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ADD)
        )
        add_button.click()

    def default_signature_id(self):
        """
        Возвращает id подписи по умолчанию
        :return 0,1,2, -1
        """
        try:
            self.driver.find_element_by_xpath(self.DEFAULT0)
            return 0
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath(self.DEFAULT1)
                return 1
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_xpath(self.DEFAULT2)
                    return 2
                except NoSuchElementException:
                    return -1

    def remove_first_signature(self):
        """
        Открывает окно удаления первой подписи
        :return: None
        """
        e = WebDriverWait(self.driver, 1, 0.1).until(EC.element_to_be_clickable((By.XPATH, self.REMOVE0)))
        e.click()

    def remove_second_signature(self):
        """
        Открывает окно удаления второй подписи
        :return: None
        """
        e = WebDriverWait(self.driver, 1, 0.1).until(EC.element_to_be_clickable((By.XPATH, self.REMOVE1)))
        e.click()

    def remove_third_signature(self):
        """
        Открывает окно удаления третьей подписи
        :return: None
        """
        e = WebDriverWait(self.driver, 1, 0.1).until(EC.element_to_be_clickable((By.XPATH, self.REMOVE2)))
        e.click()

    def edit_first_signature(self):
        """
        Открывает окно изменения первой подписи
        :return: None
        """
        f = WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDIT0)
        )
        f.click()

    def edit_second_signature(self):
        """
        Открывает окно изменения второй подписи
        :return: None
        """
        f = WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDIT1)
        )
        f.click()

    def edit_third_signature(self):
        """
        Открывает окно изменения третьей подписи
        :return: None
        """
        f = WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDIT2)
        )
        f.click()

    def first_signature_exists(self):
        """
        Проверяет, существует ли первая подпись
        :return: True, False
        """
        try:
            self.driver.find_element_by_xpath(self.CONTAINER0)
            return True
        except NoSuchElementException:
            return False

    def second_signature_exists(self):
        """
        Проверяет, существует ли вторая подпись
        :return: True, False
        """
        try:
            self.driver.find_element_by_xpath(self.CONTAINER1)
            return True
        except NoSuchElementException:
            return False

    def third_signature_exists(self):
        """
        Проверяет, существует ли третья подпись
        :return: True, False
        """
        try:
            self.driver.find_element_by_xpath(self.CONTAINER2)
            return True
        except NoSuchElementException:
            return False

    def can_create_signature(self):
        """
        Проверяет, можно ли создать подпись
        :return: True, False
        """
        try:
            self.driver.find_element_by_xpath(self.ADD)
            return True
        except NoSuchElementException:
            return False

    def first_signature_name(self):
        """
        Возвращает имя отправителя для первой подписи
        :return: имя отправителя
        """
        return WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NAME0).text
        )

    def second_signature_name(self):
        """
        Возвращает имя отправителя для второй подписи
        :return: имя отправителя
        """
        return WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NAME1).text
        )

    def third_signature_name(self):
        """
        Возвращает имя отправителя для третьей подписи
        :return: имя отправителя
        """
        return WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NAME2).text
        )

    def set_first_signature_default(self):
        """
        Устанавливает первую подпись по умолчанию
        """
        f = WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SETACTIVE0)
        )
        f.click()

    def set_second_signature_default(self):
        """
        Устанавливает вторую подпись по умолчанию
        """
        f = WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SETACTIVE1)
        )
        f.click()

    def set_third_signature_default(self):
        """
        Устанавливает третью подпись по умолчанию
        """
        f = WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SETACTIVE2)
        )
        f.click()
