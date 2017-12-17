# -*- coding: utf-8 -*-

import os
import urlparse

from selenium.webdriver.support.wait import WebDriverWait


class Page:
    BASE_URL = 'https://ok.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthForm:
    LOGIN = '//input[@id="field_email"]'
    PASSWORD = '//input[@id="field_password"]'
    LOGIN_BUTTON = '//input[@class="button-pro __wide"]'

    def __init__(self, driver):
        self.driver = driver

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()


class AuthPage(Page):
    def login(self):
        user_login = os.environ['LOGIN']
        user_password = os.environ['PASSWORD']

        auth_form = AuthForm(self.driver)#self.form
        auth_form.set_login(user_login)
        auth_form.set_password(user_password)
        auth_form.submit()


class MainPage(Page):
    USERNAME = '//h1[@class="mctc_name_tx bl"]'
    SEARCH = 'field_query'
    SEARCH_SUGGESTIONS = 'hook_Block_ToolbarSuggestions'
    SEARCH_SUGGESTIONS_SHOWALL_LINK = '//div[@id="toolbar_search"]//div[@class="search_suggest_show-all"]'
    SEARCH_OVERLAY = '//div[@id="toolbar_search"]/div[@class="layer_ovr"]'
    SEARCH_BTN = 'lsBtn'
    SEARCH_RESULTS = 'searchResults'

    def get_username(self):
        return self.driver.find_element_by_xpath(self.USERNAME).text

    def search(self, some_string):
        self.driver.find_element_by_id(self.SEARCH).send_keys(some_string)

    def get_search_suggestions_on_page(self):
        return self.driver.find_element_by_id(self.SEARCH_SUGGESTIONS)

    def get_search_suggestions_showall_text(self):
        return self.driver.find_element_by_xpath(self.SEARCH_SUGGESTIONS_SHOWALL_LINK).text

    def get_search_overlay_on_page(self):
        return self.driver.find_element_by_xpath(self.SEARCH_OVERLAY)

    def submit_search(self):
        self.driver.find_element_by_id(self.SEARCH_BTN).click()


class SearchPage(Page):
    MENU = '//div[@id="categoriesList"]/ul[@class="main-menu"]/li'
    MENU_ACTIVE = '//div[@id="categoriesList"]/ul[@class="main-menu"]//span[contains(@class, "__active")]'
    SEARCH_INPUT = '//input[@id="query_usersearch"]'
    SEARCH_CANCEL = 'livesearch_cancelId'
    FILTER_TAGS = '//div[@id="filterTags"]/div[@class="tag"]'
    FILTER_CLEAR = '//div[@id="filterTags"]/a'

    def get_menu(self):
        return self.driver.find_elements_by_xpath(self.MENU)

    def get_menu_active(self):
        return self.driver.find_element_by_xpath(self.MENU_ACTIVE).text

    def get_search_input(self):
        return self.driver.find_element_by_xpath(self.SEARCH_INPUT)

    def get_search_cancel(self):
        return self.driver.find_element_by_id(self.SEARCH_CANCEL)

    def get_filter_tags(self):
        return self.driver.find_elements_by_xpath(self.FILTER_TAGS)

    def clear_filter_result(self):
        self.driver.find_element_by_xpath(self.FILTER_CLEAR).click()


class SearchFilterPage(Page):
    FEMALE = '//div[@id="facets"]//div[@data-aid="PS_Click_Gender_Female"]'
    FROM_AGE = '//div[@id="facets"]//select[@id="field_fromage"]'
    TILL_AGE = '//div[@id="facets"]//select[@id="field_tillage"]'
    GENDER_BLOCK = '//div[@id="facets"]//div[@id="gender"]'
    GENDER_TITLE = '//div[@id="facets"]//div[@id="gender"]/div[@class="gs_filter_t"]'

    def _from_age_selector(self, age):
        return '//div[@id="facets"]//select[@id="field_fromage"]/option[@value="' + str(age) + '"]'
    def _till_age_selector(self, age):
        return '//div[@id="facets"]//select[@id="field_tillage"]/option[@value="' + str(age) + '"]'


    def set_female(self):
        self.driver.find_element_by_xpath(self.FEMALE).click()

    def click_from_age(self):
        self.driver.find_element_by_xpath(self.FROM_AGE).click()

    def click_from_age_select(self, age):
        selector = self._from_age_selector(age)
        self.driver.find_element_by_xpath(selector).click()

    def click_till_age(self):
        self.driver.find_element_by_xpath(self.TILL_AGE).click()

    def click_till_age_select(self, age):
        selector = self._till_age_selector(age)
        self.driver.find_element_by_xpath(selector).click()

    def get_gender_block(self):
        return self.driver.find_element_by_xpath(self.GENDER_BLOCK)

    def get_gender_title(self):
        return self.driver.find_element_by_xpath(self.GENDER_TITLE)
