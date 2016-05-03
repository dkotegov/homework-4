# -*- coding: utf-8 -*-
__author__ = 'niggor'
from drugs.pages.main_page import Component, Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from urlparse import urljoin
import requests

class CompanyPage(Page):
    PATH = '/company/list_moscow/bolnitsy/'

    @property
    def dropdown_list(self):
        return DropdownList(self.driver)


class DropdownList(Component):
    DROPDOWN_BUTTON = "div.dropdown__field.js-dropdown__button"
    ELEMENT_XPATH = "//span[text() = '%s']"
    SCROLL_SCRIPT = "return arguments[0].scrollIntoView();"
    VALUE = ".dropdown__text.js-dropdown__text"

    def open_dropdown_list(self):
        self.driver.find_element_by_css_selector(self.DROPDOWN_BUTTON).click()

    def element_is_visible(self, list_element):
        return self.driver.find_element_by_xpath(self.ELEMENT_XPATH % list_element).is_displayed()

    def scroll(self, text):
        item = self.driver.find_element_by_xpath(self.ELEMENT_XPATH % text)
        self.driver.execute_script(self.SCROLL_SCRIPT, item)
        return item

    def get_value(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR,self.VALUE))
        )
        return self.driver.find_element_by_css_selector(self.VALUE).text

    def select_metro_station(self, metro_station):
        item = self.scroll(metro_station)
        item.click()


