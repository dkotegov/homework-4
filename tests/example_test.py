# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class Page(object):
    BASE_URL = 'https://cloud.mail.ru/home/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthForm(Component):
    LOGIN = '//input[@name="username"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'
    LOGIN_BUTTON = '//a[text()="Войти"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def next(self):


    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    # @property
    # def top_menu(self):
    #     return TopMenu(self.driver)


class ExampleTest(unittest.TestCase):
    USEREMAIL = 'adolgavintest@mail.ru'
    PASSWORD = 'homework1234'

    def setUp(self):
        browser = 'CHROME'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def runTest(self):
        self.driver.get("https://cloud.mail.ru/home/")
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USEREMAIL)
        auth_form.next()
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()
