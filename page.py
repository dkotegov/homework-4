# -*- coding: utf-8 -*-

import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
    BASE_URL = 'https://deti.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class NamesPage(Page):
    PATH = 'names/'


class Menu(object):
    def __init__(self, driver):
        self.driver = driver

    def get_logo(self):
        return self.driver.find_element_by_xpath(self.LOGO)

    def get_forum(self):
        return self.driver.find_element_by_xpath(self.FORUM)
