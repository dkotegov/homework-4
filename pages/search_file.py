import time

import urllib.parse as urlparse

from selenium.common.exceptions import NoSuchElementException

from pages.default import Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchFilePage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home'

    SEARCH_FILE = 'div[id="portal-menu__toolbar"] button[name="searchSubmit"]'
    SELECTED_SEARCH_FILE = 'div[id="portal-menu__toolbar"] span[class^="pm-toolbar__search__params__text"]'
    DROPDOWN_FILE_TYPES = 'div[id="portal-menu__toolbar"] span[class^="js-dropdown-button"]'
    SEARCH_FILE_TYPE = 'div[id="portal-menu__toolbar"] span[class^="js-dropdown"]'
    INPUT_SEARCH_FILE = 'div[id="portal-menu__toolbar"] input'
    EMPTY_FILE_FAVICON = 'div[class*="Empty__title"]'
    FOUND_FILES = 'a[class*="DataListItem"]'
    UPLOAD_FILE = 'div[data-name="upload"]'
    CLOSE_NOTION = 'div[class*="Bubble__close"]'
    INPUT_FILE = 'input[type=file]'
    UPLOAD_FILE_POPUP = 'div[data-qa-modal="upload-dlg"]'

    def click_on_search_button(self):
        self.driver.find_element_by_css_selector(self.SEARCH_FILE).click()

    def click_on_input(self):
        self.driver.find_element_by_css_selector(self.INPUT_SEARCH_FILE).click()

    def remove_input(self):
        self.driver.find_element_by_css_selector(self.INPUT_SEARCH_FILE).send_keys(Keys.BACKSPACE)

    def set_filename(self, filename):
        self.driver.find_element_by_css_selector(self.INPUT_SEARCH_FILE).send_keys(filename)

    def open_dropdown_search_types(self):
        self.driver.find_element_by_css_selector(self.DROPDOWN_FILE_TYPES).click()

    def select_search_type(self, search_type):
        for file in self.driver.find_elements_by_css_selector(self.SEARCH_FILE_TYPE):
            if file.text == search_type:
                file.click()
                return

    def click_on_upload(self):
        self.driver.find_element_by_css_selector(self.UPLOAD_FILE).click()

    def click_on_close_notion(self):
        try:
            self.driver.find_element_by_css_selector(self.CLOSE_NOTION).click()
        except Exception:
            return

    def upload_file(self, file_path):
        self.driver.find_element_by_css_selector(self.INPUT_FILE).send_keys(file_path)

    def wait_popup_to_close(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.UPLOAD_FILE_POPUP)))
        except Exception as e:
            return


    def check_selected_type(self, search_type):
        try:
            if self.driver.find_element_by_css_selector(self.DROPDOWN_FILE_TYPES).text == search_type:
                return True
        except NoSuchElementException:
            return False
        return False

    def check_search_result_is_empty(self):
        try:
            self.driver.find_element_by_css_selector(self.EMPTY_FILE_FAVICON)
        except NoSuchElementException:
            return True
        return False

    def check_search_file_is_found(self, filename):
        for file in self.driver.find_elements_by_css_selector(self.FOUND_FILES):
            if file.get_attribute('data-qa-name') == filename:
                return True
        return False