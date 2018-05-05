# -*- coding: utf-8 -*-
from Components.component import Component


class AuthForm(Component):
    LOGIN = '//input[@id="field_email"]'
    PASSWORD = '//input[@id="field_password"]'
    SUBMIT = '//input[@class="button-pro __wide"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
