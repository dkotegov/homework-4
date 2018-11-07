# -*- coding: utf-8 -*-

import os

import urlparse

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class ElementWaiter(object):

    @staticmethod
    def whait(driver, by, locator):
        try:
            delay = 30
            elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((by, locator)))
            print "Page is ready!"
            return elem
        except TimeoutException:
            print "Loading took too much time!"
            return None

    @staticmethod
    def whait_by_xpath(driver, locator):
        try:
            delay = 30
            elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, locator)))
            print "Page is ready!"
            return elem
        except TimeoutException:
            print "Loading took too much time!"
            return None


class Page(object):
    BASE_URL = 'https://mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)

class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthMail(self.driver)

class MailPage(Page):
    SETTINGS_MENU = '//span[@class="button2__wrapper"]'
    SETTINGS_ROW = '//div[@class="list list_hover-support"]/div[13]'
    

    def open_settings_menu(self):
        elem = ElementWaiter.whait(driver = self.driver, by = By.XPATH, locator = self.SETTINGS_MENU)
        elem.click()

    def open_settings_page(self):
        elem = ElementWaiter.whait(driver = self.driver, by = By.XPATH, locator = self.SETTINGS_ROW)
        elem.click()

class SettingsPage(Page):
    FILTERING_RULES = '//a[@href="/settings/filters?octaviusMode=1"]'
    CREATE_NEW_FILTERING = '//a[@href="/settings/filters?action=edit"]'

    def open_filtering_rules(self):
        elem = ElementWaiter.whait(driver = self.driver, by = By.XPATH, locator = self.FILTERING_RULES)
        elem.click()
    
    def create_new_filter(self):
        elem = ElementWaiter.whait(driver = self.driver, by = By.XPATH, locator = self.CREATE_NEW_FILTERING)
        elem.click()

class Component(object):
    def __init__(self, driver):
        self.driver = driver

class AuthMail(Component):
    LOGIN = 'mailbox:login'
    PASSWORD = 'mailbox:password'
    SUBMIT = '//input[@class="o-control"][@type="submit"]'

    def set_login(self, login):
        self.driver.find_element_by_id(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_id(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    @property
    def menu(self):
        return MailPage(self.driver)

class OpenFilterSettings(Component):

    def open(self, username, password):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_mail = auth_page.form
        auth_mail.set_login(username)
        auth_mail.set_password(password)
        auth_mail.submit()
        
        mail_page = MailPage(self.driver)
        mail_page.open_settings_menu()
        mail_page.open_settings_page()

        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        settings_page = SettingsPage(self.driver)
        settings_page.open_filtering_rules()