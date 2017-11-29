# -*- coding: utf-8 -*-

import os
import urlparse


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

WAIT_TIME = 20


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
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True

    def value(self):
        self.driver.find_element_by_xpath(self.SEARCH_FIELD).text

    def is_status(self, status):
        xpath = './/span[text()="%s"]' % status
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True


class Categories(Component):
    CATEGORIES_DIV = '//div[@class="gs_filter_column"]'
    CATEGORY_FIELD = '//div[@class="gs_filter_t"]'

    def CheckExists(self, name):
        try:
            elem = WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located((By.XPATH, './/div[text()="%s"]' % name)))
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True


    def Set(self, name):
        xpath = './/div[text()="%s"]' % name
        WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(
            (By.XPATH, xpath))).click()


class NavBar(Component):
    GROUP_LINK = '//span[@data-field_mode="Groups"]'
    GAME_LINK = '//span[@data-field_mode="Games"]'
    MUSIC_LINK = '//span[@data-field_mode="Music"]'
    MOVIE_LINK = '//span[@data-field_mode="Movie"]'
    MENU_LIST = '//ul[@class="main-menu"]'

    def try_click(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except (NoSuchElementException, ElementNotVisibleException):
            pass

    def goto_groups(self):
        self.try_click(self.GROUP_LINK)

    def goto_games(self):
        self.try_click(self.GAME_LINK)

    def goto_music(self):
        self.try_click(self.MUSIC_LINK)

    def goto_movies(self):
        self.try_click(self.MOVIE_LINK)

    def is_all_empty(self):
        empty_xpath = './/span[@class="gs_tab main-menu_a __empty"]'
        menu_list = WebDriverWait(self.driver, WAIT_TIME).until(EC.presence_of_all_elements_located(
            (By.XPATH, empty_xpath)))
        return len(menu_list) == 4
        


class SearchResult(Component):
    EMPTY_RESULT_DIV = './/div[@class="stub-empty __search"]'
    RESULT_LIST = './/div[@class="gs_result_list"]'
    MUSIC_BEST_SEARCH = './/div[@class="mus_h2"]/span'

    def is_empty(self):
        try:
            self.driver.find_element_by_xpath(self.EMPTY_RESULT_DIV)
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True

    def contains(self, value):
        try:
            elem = WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located((By.XPATH, './/a[text()="%s"]' % value)))
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True


    def music_best_search(self):
        return WebDriverWait(self.driver, WAIT_TIME).until(
            EC.visibility_of_element_located((By.XPATH, self.MUSIC_BEST_SEARCH))).text
