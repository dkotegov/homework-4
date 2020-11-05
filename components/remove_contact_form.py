# -*- coding: utf-8 -*-

import time

from .base import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, WebDriverException


class RemoveContactFormLocators:
    def __init__(self):
        self.confirm_removal = '//button[@data-test-id="addressbook-notification-popup-submit"]'
        self.decline_removal = '//button[@data-test-id="addressbook-notification-popup-cancel"]'
        self.cross = '//div[@data-test-id="cross"]'


class RemoveContactForm(Component):

    def __init__(self, driver):
        super(RemoveContactForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 15)

        self.locators = RemoveContactFormLocators()

    def confirm_removal(self):
        """
        Подтверждает удаление
        """
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.confirm_removal)))
        element.click()

    def decline_removal(self):
        """
        Отклоняет удаление
        """
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.decline_removal)))
        element.click()

    def cancel_removal(self):
        """
        Нажимает на крестик в окне удаления
        """
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.cross)))
        element.click()
