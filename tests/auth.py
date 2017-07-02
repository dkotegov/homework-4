# -*- coding: utf-8 -*-
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.event_page.event_page import Notification
from tests.utils import wait_for_element_load, Page, Component

class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

class AuthForm(Component):
    LOGIN_POPUP = '//div[@id="popup-login"]'
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'
    LOGIN_BUTTON = '//a[text()="Вход для участников"]'

    def open_form(self):
        self._wait_for_xpath(self.LOGIN_BUTTON)
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self._wait_for_xpath(self.LOGIN)
        self._wait_for_xpath(self.LOGIN_POPUP)
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

class LogoutInterface(Component):
    MENU = '//div[@id="dropdown-user-trigger"]'
    LOGOUT = '//a[@class="logout"]'

    def logout(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.MENU)))
        self.driver.find_element_by_xpath(self.MENU).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.LOGOUT)))
        self.driver.find_element_by_xpath(self.LOGOUT).click()


def authenticate(driver, another=False):
    EMAIL = os.environ['LOGIN' if not another else 'LOGIN2']
    PASSWORD = os.environ['PASSWORD' if not another else 'PASSWORD2']

    auth_page = AuthPage(driver)
    auth_page.open()
    auth_form = auth_page.form
    auth_form.open_form()
    auth_form.set_login(EMAIL)
    auth_form.set_password(PASSWORD)
    auth_form.submit()
    wait_for_element_load(driver, (By.XPATH, '//a[text()="Блоги "]'))

def logout(driver):
    logout_interface = LogoutInterface(driver)
    logout_interface.logout()