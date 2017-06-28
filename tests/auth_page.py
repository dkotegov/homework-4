# -*- coding: utf-8 -*-

import os
from utils import *

class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

class AuthForm(Component):
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'
    LOGIN_BUTTON = '//a[text()="Вход для участников"]'

    def open_form(self):
        self._wait_for_xpath(self.LOGIN_BUTTON)
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self._wait_for_xpath(self.LOGIN)
        self._wait_for_xpath(self.SUBMIT)
        self.driver.find_element_by_xpath(self.LOGIN).click()
        self.driver.find_element_by_xpath(self.LOGIN).clear()
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self._wait_for_xpath(self.PASSWORD)
        self.driver.find_element_by_xpath(self.PASSWORD).click()
        self.driver.find_element_by_xpath(self.PASSWORD).clear()
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self._wait_for_xpath(self.SUBMIT)
        self.driver.find_element_by_xpath(self.SUBMIT).click()

def authenticate(driver):
    EMAIL = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    auth_page = AuthPage(driver)
    auth_page.open()
    auth_form = auth_page.form
    auth_form.open_form()
    auth_form.set_login(EMAIL)
    auth_form.set_password(PASSWORD)
    auth_form.submit()
    wait_for_element_load(driver, (By.XPATH, '//a[text()="Блоги "]'))
    print 'authenticated!'

# class TopMenu(Component):
#     USERNAME = '//a[@class="username"]'
#
#     def get_username(self):
#         return WebDriverWait(self.driver, 30, 0.1).until(
#             lambda d: d.find_element_by_xpath(self.USERNAME).text
#         )
