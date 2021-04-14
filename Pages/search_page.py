from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os


class SearchPage(Page):
    PATH = '/search'
    SEARCH = '//input[@name="search"]'
    ELEMENT = '//div[contains(text(),"'
    ELEMENT_USER = '//a[contains(text(),"'

    def fill_search(self, string):
        self.driver.find_element_by_xpath(self.SEARCH).send_keys(string)

    def check_search(self, string):
        elem = self.ELEMENT + string + '")]'
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, elem)))
        except TimeoutException:
            return False
        else:
            return True

    def check_search_user(self, string):
        elem = self.ELEMENT_USER + string + '")]'
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, elem)))
        except TimeoutException:
            return False
        else:
            return True