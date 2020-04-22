# -*- coding: utf-8 -*-

import os

import unittest
from time import sleep
from urllib.parse import urljoin

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    BASE_URL = 'https://fwork.live/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(Component):
    LOGIN = '//input[@name="email"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//button[@type="submit"]'
    LOGIN_BUTTON = 'button.btn.btn_primary[type="submit"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


# class LoginTest(unittest.TestCase):
#     EMAIL = 'da@mail.ru'
#     PASSWORD = '123456'
#     BLOG = 'Флудилка'
#     TITLE = u'ЗаГоЛоВоК'
#     MAIN_TEXT = u'Текст под катом! Отображается внутри топика!'
#
#     def setUp(self):
#         browser = os.environ.get('BROWSER', 'CHROME')
#
#         self.driver = Remote(
#             command_executor='http://127.0.0.1:4444/wd/hub',
#             desired_capabilities=getattr(DesiredCapabilities, browser).copy()
#         )
#
#     def tearDown(self):
#         self.driver.quit()
#
#     def test(self):
#         auth_page = AuthPage(self.driver)
#         auth_page.open()
#
#         auth_form = auth_page.form
#         auth_form.set_login(self.EMAIL)
#         auth_form.set_password(self.PASSWORD)
#         auth_form.submit()




