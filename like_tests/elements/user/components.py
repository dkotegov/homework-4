# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait

from like_tests.elements.component import *


class AuthForm(Component):
    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@class="button-pro __wide"]'
    LOGIN_HREF = '//a[@class="filter_i __active js-login-nav js-login-login"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def is_logged_out(self):
        WebDriverWait(self.driver, self.TIMEOUT, self.POLL_FREQUENCY).until(
            lambda d: d.find_element_by_xpath(self.LOGIN_HREF)
        )
        return True


class UserHeader(Clickable):
    CLICK = '//h1[@class="mctc_name_tx bl"]'

    def get_username(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.POLL_FREQUENCY).until(
            lambda d: d.find_element_by_xpath(self.CLICK).text
        )


class LogoutButton(Clickable):
    CLICK = '//a[@class="x-ph__link x-ph__link_last"]'


class LogoutConfirmButton(Clickable):
    CLICK = '//input[@class="button-pro form-actions_yes"]'
