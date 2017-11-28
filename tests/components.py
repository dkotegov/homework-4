# -*- coding: utf-8 -*-

import os
import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

WAIT_TIME = 10


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@data-l="t,loginButton"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class SearchField(Component):
    SEARCH_FIELD = '//input[@name="st.query"]'
    CLEAR_BUTTON = '//a[@class="search-input_control search-input_close"]'
    SEARCH_STATUS = '//div[@class="portlet_h_name_t"]/span'

    def enter(self, query):
        self.driver.find_element_by_xpath(self.SEARCH_FIELD).send_keys(query)

    def clear(self):
        try:
            self.driver.find_element_by_xpath(self.CLEAR_BUTTON).click()
        except NoSuchElementException:
            return False
        return True

    def value(self):
        self.driver.find_element_by_xpath(self.SEARCH_FIELD).text

    def status(self):
        # self.driver.find_element_by_xpath(self.SEARCH_STATUS).text
        return WebDriverWait(self.driver, WAIT_TIME).until(EC.presence_of_element_located((By.XPATH, self.SEARCH_STATUS))).text


class Categories(Component):
    CATEGORIES_DIV = '//div[@class="gs_filter_column"]'

    def CheckExists(self, name):
        cat_list = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, self.CATEGORIES_DIV)))

        # print len(cat_list)
        print len(cat_list.find_elements_by_xpath('./div'))
        
        for c in cat_list.find_elements_by_xpath('./div'):
            # print c.find_element_by_xpath('.//div[@class="gs_filter_t"]').text
            if c.find_element_by_xpath('.//div[@class="gs_filter_t"]').text == name:
                return True
        return False
