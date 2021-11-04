import time

import urllib.parse as urlparse
from pages.default import Page

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class FilePreviewPage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home'

    CREATE_NEW = 'div[class*="DataListItemCreateNew"]'
    SUBMIT = 'div[data-qa-modal] button[class*="primary"]'
    SUBMIT_SHARED = 'div[data-qa-modal] button:not(.primary)'
    INPUT_FOLDER_NAME = 'div[data-qa-modal] input'
    ERROR_CLASS = 'div [class*="index__error"]'

    UPLOAD_FILE = 'div[data-name="upload"]'
    CLOSE_NOTION = 'div[class*="Bubble__close"]'
    REMOVE_RESTRICTIONS = ''

    INPUT_FILE = 'input[type=file]'
    CLOSE = 'div[data-qa-modal="upload-dlg"] div[class*="Dialog__close"]'

    def click_on_upload(self):
        self.driver.find_element_by_css_selector(self.UPLOAD_FILE).click()

    def click_on_close_notion(self):
        self.driver.find_element_by_css_selector(self.CLOSE_NOTION).click()

    def upload_file(self, file_path):
        print(file_path)
        self.driver.find_element_by_css_selector(self.INPUT_FILE).send_keys(file_path)
        self.driver.find_element_by_css_selector(self.CLOSE).click()

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
