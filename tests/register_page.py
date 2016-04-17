# -*- coding: utf-8 -*-
from page import Page
from component import Component


class RegisterPage(Page):
    PATH = u'/signup/'

    def get_form(self):
        return RegisterForm(self.driver)


class RegisterForm(Component):

    TITLE = u"//div[contains(@class, 'qc-title-row')]"

    FIRST_NAME_INPUT = u"//*[contains(@class, 'qc-firstname-row')]/span[contains(@class, 'sig2')]/input"
    FIRST_NAME_NOTIF = u"//*[contains(@class, 'qc-firstname-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'example')]"
    FIRST_NAME_ERROR = u"//*[contains(@class, 'qc-firstname-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"

    def get_first_name_notif(self):
        return self.driver.find_element_by_xpath(self.FIRST_NAME_NOTIF)

    def get_first_name_error(self):
        return self.driver.find_element_by_xpath(self.FIRST_NAME_ERROR)

    def set_first_name(self, name):
        self.driver.find_element_by_xpath(self.FIRST_NAME_INPUT).send_keys(name)

    def unfocus(self):
        self.driver.find_element_by_xpath(self.TITLE).click()