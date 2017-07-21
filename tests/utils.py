# -*- coding: utf-8 -*-
import os
import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    BASE_URL = 'http://ftest.tech-mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self, url=None):
        if url is None:
            url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    @classmethod
    def get_url(cls):
        return cls.BASE_URL + cls.PATH

    @property
    def header(self):
        return Header(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def _wait_for_xpath(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((By.XPATH, xpath)), str(self.__class__) + ': ' + xpath)

    def _clicker(self, xpath):
        self._wait_for_xpath(xpath).click()


class Header(Component):
    HEADER_PATH = '//h2[@class="page-header"]'

    def get_header_text(self):
        return self._wait_for_xpath(self.HEADER_PATH).text




class Test(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()


def wait_for_element_load(driver, element, timeout=30):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(element))
