# -*- coding: utf-8 -*-
__author__ = 'alla'
from selenium.webdriver.support.ui import WebDriverWait
from urlparse import urljoin
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from drugs.auth import TEST_USER_PASSWORD, TEST_USERNAME

class Page:
    BASE_URL = 'https://health.mail.ru/'
    PATH = ''
    AUTH_BUTTON = 'PH_authLink'
    LOGIN_NAME = 'Username'
    PASSWORD_NAME = 'Password'
    LOGIN_BUTTON = '//button[@data-uniqid="toolkit-4"]'
    TITLE = 'h1.page-info__title'
    PAGE_TIMEOUT = 50

    def __init__(self, driver):
        self.driver = driver
        self.window_handle = driver.current_window_handle

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def wait_for_another_page(self):
        old_page = self.driver.find_element_by_tag_name('html')
        WebDriverWait(self.driver, self.PAGE_TIMEOUT).until(staleness_of(old_page))

    def login(self):
        self.open_form()
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector("iframe.ag-popup__frame__layout__iframe"))
        self.set_login()
        self.set_password()
        self.submit()
        self.driver.switch_to_default_content()

    def open_form(self):
        self.driver.find_element_by_id(self.AUTH_BUTTON).click()

    def set_login(self):
        self.driver.find_element_by_name(self.LOGIN_NAME).send_keys(TEST_USERNAME)

    def set_password(self):
        self.driver.find_element_by_name(self.PASSWORD_NAME).send_keys(TEST_USER_PASSWORD)

    def submit(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def close(self):
        self.driver.close()

    def get_title(self):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.TITLE))
        )
        return self.driver.find_element_by_css_selector(self.TITLE).text

class Component(object):
    TIMEOUT = 50
    def __init__(self, driver):
        self.driver = driver

