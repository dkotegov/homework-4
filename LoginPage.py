import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    BASE_URL = 'https://m.calendar.mail.ru/login'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.BASE_URL)

    def open(self):
        url = self.BASE_URL
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

    def register(self):
        elem = self.driver.find_element_by_css_selector('.calendar-title')
        elem.click()

    def forgot_password(self):
        elem = self.driver.find_element_by_css_selector('.calendar-title')
        elem.click()

    def email_required(self):
        elem = self.driver.find_element_by_css_selector('input[name=Login]')
        validation_message = elem.get_attribute("validationMessage")

    def wait_redirect(self, url, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
