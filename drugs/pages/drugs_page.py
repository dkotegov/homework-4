# -*- coding: utf-8 -*-
__author__ = 'alla'
from drugs.pages.main_page import Component, Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import requests


class DrugsPage(Page):
    PATH = '/drug/'

    @property
    def search_form(self):
        return SearchForm(self.driver)

    @property
    def leaders_of_sells(self):
        return LeadersOfSells(self.driver)

    @property
    def catalog(self):
        return Catalog(self.driver)


class SearchForm(Component):
    INPUT_FIELD = "input.input__field.js-suggest__input"
    SUBMIT_BUTTON = 'button.button.button_color_project'
    ITEMS = 'div.entry.entry_medicament.margin_bottom_20'
    NAME = 'div.entry__name'
    SEARCH_TIMEOUT = 10

    def input(self, text):
        self.driver.find_element_by_css_selector(self.INPUT_FIELD).send_keys(text)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT_BUTTON).click()

    def items(self):
        try:
            WebDriverWait(self.driver, self.SEARCH_TIMEOUT).until(
                expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.ITEMS))
            )
            return self.driver.find_elements_by_css_selector(self.ITEMS)
        except TimeoutException:
            return None

    def get_name(self, el):
        return el.find_element_by_css_selector(self.NAME).text.split(',')[0]

    def found_drugs(self):
        items = self.items()
        return [self.get_name(item) for item in items]


class LeadersOfSells(Component):
    ITEMS = "div.entry.entry_medicament.margin_bottom_30"
    NAME = "div.entry__name"
    TITLE = '//h1[@class="page-info__title"]'

    def items(self):
        return self.driver.find_elements_by_css_selector(self.ITEMS)

    def get_name(self, el):
        return el.find_element_by_css_selector(self.NAME).text.split(',')[0]

    def go_to_drugs_page(self, title):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, title)))
        self.driver.find_element_by_link_text(title).click()

    def get_all(self):
        items = self.items()
        return [self.get_name(item) for item in items]


class Catalog(Component):
    LINK = 'a.catalog__item'

    def check_link(self, link):
        return requests.get(link).status_code == 200

    def links(self):
        items = self.driver.find_elements_by_xpath(self.LINK)
        return [item.get_attribute('href') for item in items]

    def to_link(self, text):
        self.driver.find_element_by_link_text(text).click()
