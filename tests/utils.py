# -*- coding: utf-8 -*-
import contextlib
import urlparse

from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Page(object):
    BASE_URL = 'http://ftest.tech-mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def _wait_for_xpath(self, xpath):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

def wait_for_element_load(driver, element, timeout=30):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(element))