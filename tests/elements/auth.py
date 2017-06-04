# coding=utf-8
import time

from selenium.webdriver.common.by import By

from base import *


class OpenLoginFormButton(BaseElement):
    locator = (By.XPATH, "//a[text()='Вход для участников']")


class LoginForm(BaseElement):
    locator = (By.XPATH, "//div[@id='popup-login']")


class LoginInput(BaseElement):
    locator = (By.XPATH, "//input[@name='login']")

    def super_wait(self, other):
        self.wait_for_presence()
        other.wait_for_presence()

        def el_enabled():
            other.get().click()
            self.get().click()
            return self.get_value() == ''

        start_time = time.time()
        while time.time() < start_time + 10:
            if el_enabled():
                return self
            else:
                time.sleep(0.1)
        raise Exception('Timeout waiting for element is enabled')


class PasswordInput(BaseElement):
    locator = (By.XPATH, "//input[@name='password']")


class SubmitLoginButton(BaseElement):
    locator = (By.XPATH, "//button[@name='submit_login']")
