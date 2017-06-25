# coding=utf-8
import time

from selenium.webdriver.common.by import By

from base import BaseElement


class LoginForm(BaseElement):

    def open_login_form_button(self):
        self.locator = (By.XPATH, "//a[text()='Вход для участников']")
        return self

    def login_form(self):
        self.locator = (By.XPATH, "//div[@id='popup-login']")
        return self

    def password_input(self):
        self.locator = (By.XPATH, "//input[@name='password']")
        return self

    def submit_login_button(self):
        self.locator = (By.XPATH, "//button[@name='submit_login']")
        return self

    def login_input(self):
        self.locator = (By.XPATH, "//input[@name='login']")
        return self

    # def super_wait(self, other):
    #     self.wait_for_presence()
    #     other.wait_for_presence()
    #
    #     def el_enabled():
    #         other.get().click()
    #         self.get().click()
    #         return self.get_value() == ''
    #
    #     start_time = time.time()
    #     while time.time() < start_time + 10:
    #         if el_enabled():
    #             return self
    #         else:
    #             time.sleep(0.1)
    #     raise Exception('Timeout waiting for element is enabled')


