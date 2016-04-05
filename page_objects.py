# -*- coding: utf-8 -*-

import os
import urlparse
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Component(object):

    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    REGISTERWINDOW ='//*[@id="x-ph__authForm__popup"]'
    LOGIN = '//*[@id="ph_login"]'
    DOMAIN = 'Domain'
    PASSWORD = '//*[@id="ph_password"]'
    SUBMIT = '//input[@class="x-ph__button__input"]'
    LOGIN_BUTTON = '//input[@class="nav-inner-col-try__bt"]' #TODO вынести в отдельную страницу
    ENTER_BUTTON = '//*[@id="PH_authLink"]'

    def open_page(self):
        self.driver.find_element_by_xpath(self.ENTER_BUTTON).click()
        # form = self.driver.find_element_by_xpath(self.LOGIN_BUTTON)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(form)
        # actions.click(form)
        # actions.perform()
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, self.ENTER_BUTTON)))
        # WebDriverWait(self.driver, 10).until(
        #     self.driver.find_element_by_xpath(self.ENTER_BUTTON).click()
        # )

    def open_form(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN))
        )

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    # def set_domain(self, domain):
    #     select = Select(self.driver.find_element_by_name(self.DOMAIN))
    #     select.select_by_value(domain)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class Page(object):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


    @property
    def top_menu(self):
        return TopMenu(self.driver)


class TopMenu(Component):
    USERNAME = '//*[@id="PH_user-email"]'

    def get_username(self):
        return WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )
