# coding=utf-8
from selenium.webdriver.common.by import By

from base import BaseElement


class ShowRepo(BaseElement):
    def gitignore(self):
        self.locator = (By.XPATH, "//a[contains(text(), '.gitignore')]")
        return self
