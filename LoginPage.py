import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time

class LoginPage:
    # BASE_URL = 'https://m.calendar.mail.ru/login'
    
    def __init__(self, driver):
        self.driver = driver
        # self.driver.get(self.BASE_URL)

    def open(self, url):
        # url = self.BASE_URL
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

    def enter_event_name(self, name):
        elem = self.driver.find_element_by_css_selector('.event-summary-input')
        # Clear old data
        elem.clear()
        # Enter new data
        elem.send_keys(name)

    def open_menu_plus(self):
        # elem = self.driver.find_element_by_css_selector('.header-menu-item__list')
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.header-menu-item.header-menu-item__sidebutton.header-menu-item__plus')))        
        elem.click()


    # def click_on_create_btn(self):
    #     # elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.calendar-create-item')))
    #     # # elem = self.driver.find_element_by_css_selector('div.calendar-create-item.panel-item.panel-item__marked')
    #     # elem.click()
    #     login_but = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.calendar-create-item.panel-item.panel-item__marked')))
    #     self.driver.execute_script("arguments[0].click();", login_but)
    #     element = self.driver.find_element_by_css_selector('.calendar-create-item.panel-item.panel-item__marked')
    #     ActionChains(self.driver).move_to_element(element ).click(element ).perform()

    def click_on_back_btn(self):
        time.sleep(1)
        elem = self.driver.find_element_by_css_selector('.header-menu-item__back')
        time.sleep(1)
        elem.click()

    def click_on_ok_btn(self):
        elem = self.driver.find_element_by_css_selector('.header-menu-item__ok')
        elem.click()

    def click_on_event(self):
        # self.check_event_available()
        # elem = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.panel-content:last-child')))
        time.sleep(1)
        elem = self.driver.find_element_by_css_selector('div.panel-content:last-child')
        time.sleep(1)
        elem.click()

    def get_event(self):
        # self.check_event_available()
        # elem = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.panel-content:last-child')))
        time.sleep(1)
        elem = self.driver.find_element_by_css_selector('div.panel-item-text.brief-event-title')
        time.sleep(1)
        return elem

    def get_count_of_events(self):
        time.sleep(1)
        # parent = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.panel-content')))
        childs = [x.text for x in self.driver.find_elements_by_css_selector("div.panel-item.brief-event")]
        # for c in childs:
        #     print(c)
        return len(childs)
            
    # def get_last_event_title(self):


    def click_on_edit_btn(self):
        time.sleep(1)
        elem = self.driver.find_element_by_css_selector('.header-menu-item__edit')
        time.sleep(1)
        elem.click()
        

    def click_on_remove_btn(self):
        time.sleep(1)
        elem = self.driver.find_element_by_css_selector('.button-delete')
        time.sleep(1)
        elem.click()

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
