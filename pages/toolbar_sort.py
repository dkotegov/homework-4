import time
import os
import urllib.parse as urlparse
from selenium.webdriver.common.action_chains import ActionChains

from pages.default import Page


class ToolbarSortFilesPage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home'
    SORT_DIR = 'sort_test'

    SORT_DROPDOWN = 'div[data-name="sort"]'
    ALPHABETIC = 'div[data-name="sortName"]'
    SIZE = 'div[data-name="sortSize"]'
    DATE = 'div[data-name="sortDate"]'

    ALPHABETIC_ASC_ORDER = ['a.txt', 'b.txt', 'c.txt']
    ALPHABETIC_DESC_ORDER = list(reversed(ALPHABETIC_ASC_ORDER))

    SIZE_ASC_ORDER = ['b.txt', 'c.txt', 'a.txt']
    SIZE_DESC_ORDER = list(reversed(SIZE_ASC_ORDER))

    DATE_ASC_ORDER = ['c.txt', 'b.txt', 'a.txt']
    DATE_DESC_ORDER = list(reversed(DATE_ASC_ORDER))

    def click_sort_dropdown(self):
        self.driver.find_element_by_css_selector(self.SORT_DROPDOWN).click()

    def click_sort_alphabetic(self):
        self.driver.find_element_by_css_selector(self.ALPHABETIC).click()

    def click_sort_size(self):
        self.driver.find_element_by_css_selector(self.SIZE).click()

    def click_sort_date(self):
        self.driver.find_element_by_css_selector(self.DATE).click()

