# -*- coding: utf-8 -*-
__author__ = 'niggor'
from drugs.pages.main_page import Component, Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class CompanyPage(Page):
    PATH = '/company/list_moscow/bolnitsy/'

    @property
    def dropdown_list(self):
        return DropdownList(self.driver)

    @property
    def paginator(self):
        return Paginator(self.driver)

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

class Paginator(Component):
    CURRENT_PAGE = 'span.paging__link.paging__link_active'
    PAGINATOR_TIMEOUT = 5
    ARROW_NEXT = 'a.paging__link.paging__link_nav.paging__link_nav_next'
    ARROW_PREV = 'a.paging__link.paging__link_nav.paging__link_nav_prev'
    LAST_PAGE = 'a.paging__link.paging__link_last'
    PAGINATOR_ELEM = "//a[@data-page='%s']"

    def get_current_page(self):
        WebDriverWait(self.driver, self.PAGINATOR_TIMEOUT).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.CURRENT_PAGE))
        )
        return int(self.driver.find_element_by_css_selector(self.CURRENT_PAGE).text)

    def get_last_page(self):
        WebDriverWait(self.driver, self.PAGINATOR_TIMEOUT).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.LAST_PAGE))
        )
        return int(self.driver.find_element_by_css_selector(self.LAST_PAGE).text)

    def paging_next(self):
        try:
            WebDriverWait(self.driver, self.PAGINATOR_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,self.ARROW_NEXT))
            )
            self.driver.find_element_by_css_selector(self.ARROW_NEXT).click()
            return True
        except TimeoutException:
            return False

    def go_to_page(self, n):
        try:
            WebDriverWait(self.driver, self.PAGINATOR_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.XPATH, self.PAGINATOR_ELEM % n))
            )
            self.driver.find_element_by_xpath(self.PAGINATOR_ELEM % n).click()
            return True
        except TimeoutException:
            return False

    def paging_prev(self):
        try:
            WebDriverWait(self.driver, self.PAGINATOR_TIMEOUT).until(
                expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,self.ARROW_PREV))
            )
            self.driver.find_element_by_css_selector(self.ARROW_PREV).click()
            return True
        except TimeoutException:
            return False




