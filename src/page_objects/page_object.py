# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains
import os


from .states import get_state
from src import get_credentials, get_webdriver



class PageObject(object):

    def __init__(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(2)
        self.state = None

    def open(self, url):
        self.driver.get(url)
        self.state = get_state(url)
        self.wait = WebDriverWait(self.driver, 10)

    def create_ac(self):
        self.action_chains = ActionChains(self.driver)

    def close(self):
        self.driver.close()

    def login(self):
        login , password = get_credentials()
        self.user_data = {
            'login': login,
            'password': password
        }

        login_input = self.driver.find_element_by_name('Login')
        login_input.send_keys(self.user_data['login'])

        password_input = self.driver.find_element_by_name('Password')
        password_input.send_keys(self.user_data['password'])

        continue_button = self.driver.find_element_by_tag_name('button')
        continue_button.click()

    def element_exists(self, selector):
        try:
            self.driver.find_element_by_css_selector(selector)
            return True
        except:
            return False


    
