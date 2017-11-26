# coding=utf-8
import time

from selenium.webdriver.common.by import By

from base import BaseElement


class LoginForm(BaseElement):

    def password_input(self):
        self.locator = (By.XPATH, "//input[@name='Password']")
        return self

    def submit_login_button(self):
        self.locator = (By.XPATH, "//button[@class='btn btn_stylish btn_main btn_single btn_fluid btn_form btn_responsive b-login__submit-btn']")
        return self

    def login_input(self):
        self.locator = (By.XPATH, "//input[@name='Username']")
        return self