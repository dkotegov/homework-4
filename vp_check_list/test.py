# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    BASE_URL = 'https://www.ok.ru'
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


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    LOGIN_BUTTON = '//input[value="Log in"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()


class TopMenu(Component):
    USERNAME = '//a[@class="mctc_name_tx bl"]'

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )  


class ExampleTest(unittest.TestCase):
    USERNAME = u'Илья Раков'
    USER_EMAIL = 'technopark34'
    PASSWORD = os.environ['OK_PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(self.USER_EMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        user_name = auth_page.top_menu.get_username()
        self.assertEqual(self.USER_EMAIL, user_name)
