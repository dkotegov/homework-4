# coding=utf-8
from selenium.webdriver.common.by import By

from base import BaseElement


class UserDropdown(BaseElement):
    def check_user_nav(self):
        self.locator = (By.XPATH, "//ul[@id='user-links']")
        return self

    def get_user_name(self):
        self.locator = (By.XPATH, "//div[@class='dropdown-header']/strong")
        return self

    def get_drop_down(self):
        self.locator = (By.XPATH, "//img[@class='avatar']")
        return self
