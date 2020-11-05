# -*- coding: utf-8 -*-
from base import Component

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class SignatureDeletionForm(Component):
    POPUP0 = '//div[@data-test-id="sign:0-delete-popup"]'
    POPUP1 = '//div[@data-test-id="sign:1-delete-popup"]'
    POPUP2 = '//div[@data-test-id="sign:2-delete-popup"]'

    APPROVEREMOVAL0 = POPUP0 + '//button[@data-test-id="delete"]'
    APPROVEREMOVAL1 = POPUP1 + '//button[@data-test-id="delete"]'
    APPROVEREMOVAL2 = POPUP2 + '//button[@data-test-id="delete"]'

    DECLINEREMOVAL0 = POPUP0 + '//button[@data-test-id="cancel"]'
    DECLINEREMOVAL1 = POPUP1 + '//button[@data-test-id="cancel"]'
    DECLINEREMOVAL2 = POPUP2 + '//button[@data-test-id="cancel"]'

    CROSS0 = POPUP0 + '//div[@data-test-id="cross"]'
    CROSS1 = POPUP1 + '//div[@data-test-id="cross"]'
    CROSS2 = POPUP2 + '//div[@data-test-id="cross"]'

    def approve_removing_first(self):
        """
        Подтверждает удаление первой подписи
        :return: None
        """
        b = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.APPROVEREMOVAL0)
        )
        b.click()

    def approve_removing_second(self):
        """
        Подтверждает удаление второй подписи
        :return: None
        """
        b = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.APPROVEREMOVAL1)
        )
        b.click()

    def approve_removing_third(self):
        """
        Подтверждает удаление третьей подписи
        :return: None
        """
        b = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.APPROVEREMOVAL2)
        )
        b.click()

    def decline_removing_first(self):
        """
        Отклоняет удаление первой подписи
        :return: None
        """
        b = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DECLINEREMOVAL0)
        )
        b.click()

    def decline_removing_second(self):
        """
        Отклоняет удаление второй подписи
        :return: None
        """
        b = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DECLINEREMOVAL1)
        )
        b.click()

    def decline_removing_third(self):
        """
        Отклоняет удаление третьей подписи
        :return: None
        """
        b = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DECLINEREMOVAL2)
        )
        b.click()

    def cancel_removing_first(self):
        """
        Нажимает на крестик при удалении первой подписи
        :return: None
        """
        b = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CROSS0)
        )
        b.click()

    def cancel_removing_second(self):
        """
        Нажимает на крестик при удалении второй подписи
        :return: None
        """
        b = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CROSS1)
        )
        b.click()

    def cancel_removing_third(self):
        """
        Нажимает на крестик при удалении третьей подписи
        :return: None
        """
        b = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CROSS2)
        )
        b.click()

    def is_first_hidden(self):
        """
        Показывает, скрыто ли окно удаления первой подписи
        :return: True,False
        """
        try:
            WebDriverWait(self.driver, 5, 0.1).until_not(
                self.driver.find_element_by_xpath(self.POPUP0)
            )
            return True
        except NoSuchElementException:
            return False

    def is_second_hidden(self):
        """
        Показывает, скрыто ли окно удаления второй подписи
        :return: True,False
        """
        try:
            WebDriverWait(self.driver, 5, 0.1).until_not(
                self.driver.find_element_by_xpath(self.POPUP1)
            )
            return True
        except NoSuchElementException:
            return False

    def is_third_hidden(self):
        """
        Показывает, скрыто ли окно удаления третьей подписи
        :return: True,False
        """
        try:
            WebDriverWait(self.driver, 5, 0.1).until_not(
                self.driver.find_element_by_xpath(self.POPUP2)
            )
            return True
        except NoSuchElementException:
            return False

    def is_first_open(self):
        """
        Показывает, открыто ли окно удаления третьей подписи
        :return: True,False
        """
        try:
            WebDriverWait(self.driver, 5, 0.1).until(
                self.driver.find_element_by_xpath(self.POPUP0)
            )
            return True
        except NoSuchElementException:
            return False

    def is_second_open(self):
        """
        Показывает, открыто ли окно удаления второй подписи
        :return: True,False
        """
        try:
            WebDriverWait(self.driver, 5, 0.1).until(
                self.driver.find_element_by_xpath(self.POPUP1)
            )
            return True
        except NoSuchElementException:
            return False

    def is_third_open(self):
        """
        Показывает, открыто ли окно удаления третьей подписи
        :return: True,False
        """
        try:
            WebDriverWait(self.driver, 5, 0.1).until(
                self.driver.find_element_by_xpath(self.POPUP2)
            )
            return True
        except NoSuchElementException:
            return False

    def currently_deleting(self):
        """
        Возвращает id удаляемой подписи или -1
        :return: 0,1,2, -1
        """
        try:
            self.driver.find_element_by_xpath(self.POPUP0)
            return 0
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath(self.POPUP1)
                return 1
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_xpath(self.POPUP2)
                    return 2
                except NoSuchElementException:
                    return -1
