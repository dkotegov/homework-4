import os
import unittest
import config

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

import time

class DealPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def enter_login(self, login):
        elem = self.driver.find_element_by_css_selector('input[name=Login]')
        elem.send_keys(login)

    def enter_password(self, password):
        elem = self.driver.find_element_by_css_selector('input[name=Password]')
        elem.send_keys(password)

    def login(self):
        elem = self.driver.find_element_by_css_selector('.login-button')
        elem.click()

    def wait_redirect(self, url, timeout = 15):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))