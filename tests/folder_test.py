import os
import time

import unittest
import urllib.parse as urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    BASE_URL = 'https://e.mail.ru/settings/folders'
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
    LOGIN = '//input[@name="username"]'
    NEXT = '//span[text()="Ввести пароль"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'

    def set_login(self, login):
        iframe = self.driver.find_element_by_class_name('ag-popup__frame__layout__iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def next(self):
        self.driver.find_element_by_xpath(self.NEXT).click()

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def authorize(self, login, password):
        self.set_login(login)
        self.next()
        self.set_password(password)
        self.submit()


class TopMenu(Component):
    USERNAME = 'PH_user-email'

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.USERNAME).text
        )


class FolderTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

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
        auth_form.authorize(self.LOGIN, self.PASSWORD)
        time.sleep(5)
        user_name = auth_page.top_menu.get_username()
        self.assertEqual(self.LOGIN + '@mail.ru', user_name)
