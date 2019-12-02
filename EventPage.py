import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time

class EventPage:
    # BASE_URL = 'https://m.calendar.mail.ru/login'
    
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

    def enter_event_name(self, name):
        elem = self.driver.find_element_by_css_selector('.event-summary-input')
        # Clear old data
        elem.clear()
        # Enter new data
        elem.send_keys(name)

    def open_menu_plus(self):
        elem = self.wait_presence_located('div.header-menu-item.header-menu-item__sidebutton.header-menu-item__plus')        
        elem.click()


    def click_on_back_btn(self):
        elem = self.wait_render_btn('.header-menu-item__back')
        elem.click()

    def click_on_ok_btn(self):
        elem = self.wait_render_btn('.header-menu-item__ok')
        elem.click()

    def click_on_first_event(self):
        # childs = self.driver.find_elements_by_css_selector("div.panel-item.brief-event")
        elem = self.wait_render_btn('div.panel-item.brief-event')
        elem.click()

    def get_first_event(self):
        elems = self.driver.find_elements_by_css_selector('div.panel-item-text.brief-event-title')
        for elem in elems:
            print('elem: %s' % elem.text)
        # The last element
        return elems[0]

    def get_count_of_events(self):
        self.wait_presence_located('div.panels-container')
        childs = self.driver.find_elements_by_css_selector("div.panel-item.brief-event")
        return len(childs)

    def create_event(self, name):
        self.open_menu_plus()
        self.enter_event_name(name)
        self.click_on_ok_btn()

    def click_on_edit_btn(self):
        elem = self.wait_render_btn('.header-menu-item__edit')
        elem.click()
        

    def click_on_remove_btn(self):
        elem = self.wait_render_btn('.button-delete')
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

    def wait_redirect(self, url, timeout = 15):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
    
    def wait_render_btn(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    
    def wait_presence_located(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_invisible(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))