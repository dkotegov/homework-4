# coding=utf-8
import time

from selenium.webdriver.common.by import By

from base import BaseElement


class LoginForm(BaseElement):

    def login_input(self):
        self.locator = (By.XPATH, "//input[@name='login']")
        return self

    def password_input(self):
        self.locator = (By.XPATH, "//input[@name='password']")
        return self

    def sign_in_button(self):
        self.locator = (By.XPATH, "//input[@name='commit']")
        return self


