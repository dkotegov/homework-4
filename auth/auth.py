import sys
from selenium import webdriver

from components.base_component import BaseComponent
from components.page import Page


class AuthPage(Page):

    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(BaseComponent):
    EMAIL_INPUT = "//input[@id='field_email']"
    PASSWORD_INPUT = "//input[@id='field_password']"
    SUBMIT_BUTTON = "//input[@class='button-pro __wide']"

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

    def full_auth(self, login, password):
        self.set_login(login)
        self.set_password(password)
        self.submit()