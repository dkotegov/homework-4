# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from states import get_state
from header_object import HeaderObject
from main_view_object import MainViewObject
from src import get_credentials, get_webdriver
from src.page_objects import PageObject


class InitPage(PageObject):

    def click_inbox(self):
        inbox_locator = (By.CSS_SELECTOR, 'div[data-qa-id="folder-name:name:Входящие"]')
        filter_control = self.wait.until(EC.presence_of_element_located(inbox_locator))
        self.wait.until(EC.element_to_be_clickable(inbox_locator))
        filter_control.click()

    def get_header_page_object(self):
        element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-qa-id="portal"]'))
        )
        return HeaderObject(element, self.wait, self.write_current_html)

    def get_main_page_object(self):
        return MainViewObject(None, self.wait, self.write_current_html)

    def write_current_html(self, filename):
        with open(filename, 'w') as out:
            out.write(self.driver.page_source.encode('utf-8').strip())


    
        

    
