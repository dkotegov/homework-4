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


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '//input[@name="username"]'
    NEXT = '//*[@id="root"]/div/div/div/div/div/form/div[2]/div[2]/div[3]/div/div[1]/button/span'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//*[@id="root"]/div/div/div/div/div/form/div[2]/div/div[3]/div/div[1]/div/button/span'

    def set_login(self, login):
        iframe = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div/iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def next(self):
        self.driver.find_element_by_xpath(self.NEXT).click()

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


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
        auth_form.set_login(self.LOGIN)
        auth_form.next()
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()
        self.assertEqual(1 + 2, 3)
