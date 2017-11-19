# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait

from like_tests.elements.component import Component


class AuthForm(Component):
    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@class="button-pro __wide"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class UserHeader(Component):
    USERNAME = '//h1[@class="mctc_name_tx bl"]'
    TIMEOUT = 5
    POLL_FREQUENCY = 0.1

    def get_username(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.POLL_FREQUENCY).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )