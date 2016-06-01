# -*- coding: utf-8 -*-
__author__ = 'niggor'
from drugs.pages.main_page import Component, Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import requests


class CompaniesPage(Page):
    PATH = '/company/list_moscow/'

    @property
    def search(self):
        return Search(self.driver)

    @property
    def company_list(self):
        return CompanyList(self.driver)

    @property
    def make_an_appointment(self):
        return MakeAnAppointment(self.driver)


class Search(Component):
    INPUT = 'input.input__field.js-suggest__input'
    SUBMIT_BUTTON = 'button.button.button_color_project'
    FOUND_COMPANY = 'div.entry.entry_reference.margin_bottom_20'

    def input(self, text):
        self.driver.find_element_by_css_selector(self.INPUT).send_keys(text)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT_BUTTON).click()

    def found_companies(self):
        return self.driver.find_elements_by_css_selector(self.FOUND_COMPANY)


class CompanyList(Component):
    LINK = '.list__item .list__text'

    def links(self):
        items = self.driver.find_elements_by_css_selector(self.LINK)
        return [item.get_attribute('href') for item in items]

    def check_link(self, link):
        return requests.get(link).status_code == 200

    def get_all_companies(self):
        list = self.driver.find_elements_by_css_selector(self.LINK)
        return [i.text for i in list]

    def go_to_company_page(self, query):
        WebDriverWait(self.driver, 50).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, query))
        )
        self.driver.find_element_by_link_text(query).click()


class MakeAnAppointment(Component):
    BUTTON = 'a.button.button_color_project'
    TITLE = 'div.page-info__title'

    def submit(self):
        WebDriverWait(self.driver, 50).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.BUTTON))
        )
        self.driver.find_element_by_css_selector(self.BUTTON).click()

    def get_title(self):
        return self.driver.find_element_by_css_selector(self.TITLE).text