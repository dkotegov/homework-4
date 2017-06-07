# coding=utf-8
from selenium.webdriver.common.by import By

from base import BaseElement

class RemoveButtons(BaseElement):

    def submit_remove_button(self):
        self.locator = (By.XPATH, "//input[@name='submit']")
        return self

    def cancel_remove_button(self):
        self.locator = (By.XPATH, "//button[@name='cancel']")
        return self
