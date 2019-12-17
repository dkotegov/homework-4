import os
import unittest
import config

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    def enter_deal_name(self, name):
        elem = self.driver.find_element_by_css_selector('.todo-new-summary-input')
        elem.send_keys(name)
    
    def click_on_name_deal(self):
        elem = self.driver.find_element_by_css_selector('.todo-new-main__disabled')
        elem.click()

    def click_on_today_btn(self):
        elem = self.driver.find_element_by_css_selector('.todo-new-main')
        elem.click()

    def click_on_add_btn(self):
        elem = self.driver.find_element_by_css_selector('.button-create')
        elem.click()
    
    def checkDeal(self):
        elem = self.driver.find_element_by_css_selector('.panel-item-content').text
        return elem


    def wait_redirect(self, url, timeout = 15):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))