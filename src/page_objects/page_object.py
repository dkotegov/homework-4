# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .states import get_state
from src import get_credentials, get_webdriver


class PageObject(object):

    def __init__(self):
        self.driver = get_webdriver()
        self.driver.set_window_size(1920, 1080)
        self.state = None

    def open(self, url):
        self.driver.get(url)
        self.state = get_state(url)
        self.wait = WebDriverWait(self.driver, 10)

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


    
        

    
