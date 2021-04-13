import os

import unittest
from selenium import webdriver
import urllib.parse as urlparse
import time

from tests.example_test import ExampleTest


class Page(object):
    BASE_URL = 'http://kino-park.online/'
    SECUREBUTTON = '//button[@id="details-button"]'
    GO = '//a[@id="proceed-link"]'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.find_element_by_xpath(self.SECUREBUTTON).click()
        self.driver.find_element_by_xpath(self.GO).click()
        self.driver.maximize_window()


class SettingPage(Page):
    PATH = '/profileChange'

    @property
    def form_change_password(self):
        return PasswordChange(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class PasswordChange(Component):
    OLD = '//input[@placeholder="Старый пароль"]'
    NEW = '//input[@placeholder="Новый пароль"]'
    REPEAT = '//input[@placeholder="Повторите новый пароль"]'
    SUBMIT = '//button[text()="Сохранить"]'

    def set_old(self, old):
        self.driver.find_element_by_xpath(self.OLD).send_keys(old)

    def set_new(self, new):
        self.driver.find_element_by_xpath(self.NEW).send_keys(new)
        self.driver.find_element_by_xpath(self.REPEAT).send_keys(new)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class PasswordChangeTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth = ExampleTest()
        ExampleTest.test(auth)
        setting_page = SettingPage(self.driver)
        setting_page.open()
        time.sleep(10)
