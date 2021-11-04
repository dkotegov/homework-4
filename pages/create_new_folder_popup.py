import time

import urllib.parse as urlparse
from pages.default import Page

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class CreateNewFolderPopupPage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home'

    CREATE_NEW = 'div[class*="DataListItemCreateNew"]'
    CREATE_NEW_FOLDER = 'div[data-name="createFolder"]'
    SUBMIT = 'div[data-qa-modal] button[class*="primary"]'
    SUBMIT_SHARED = 'div[data-qa-modal] button:not(.primary)'
    INPUT_FOLDER_NAME = 'div[data-qa-modal] input'
    ERROR_CLASS = 'div [class*="index__error"]'

    def click_on_create_new(self):
        self.driver.find_element_by_css_selector(self.CREATE_NEW).click()

    def click_on_create_new_folder(self):
        self.driver.find_element_by_css_selector(self.CREATE_NEW_FOLDER).click()

    def click_on_submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()

    def click_on_submit_shared(self):
        self.driver.find_element_by_css_selector(self.SUBMIT_SHARED).click()

    def click_on_input(self):
        self.driver.find_element_by_css_selector(self.INPUT_FOLDER_NAME).click()

    def remove_input(self):
        self.driver.find_element_by_css_selector(self.INPUT_FOLDER_NAME).send_keys(Keys.BACKSPACE)

    def long_input(self):
        res_string = ''
        for i in range(322):
            res_string += 'a'

        self.driver.find_element_by_css_selector(self.INPUT_FOLDER_NAME).send_keys(res_string)

    def checkErrorExists(self):
        try:
            self.driver.find_element_by_css_selector(self.INPUT_FOLDER_NAME)
        except Exception:
            return False
        return True
