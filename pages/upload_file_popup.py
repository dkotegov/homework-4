import time

import urllib.parse as urlparse
from pages.default import Page

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class UploadFilePopupPage(Page):
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
    UPLOAD_BIG_FILE = 'div[data-qa-modal="upload-big-file"]'
    REMOVE_THE_RESTRICTION = 'a[class*="UploadDialog__link"]'

    def click_on_upload(self):
        self.driver.find_element_by_css_selector(self.UPLOAD_FILE).click()

    def click_on_close_notion(self):
        self.driver.find_element_by_css_selector(self.CLOSE_NOTION).click()

    def upload_file(self, file_path):
        self.driver.find_element_by_css_selector(self.INPUT_FILE).send_keys(file_path)

    def check_error_exists(self):
        try:
            self.driver.find_element_by_css_selector(self.UPLOAD_BIG_FILE)
        except:
            return False
        return True

    def click_remove_the_restriction(self):
        self.driver.find_element_by_css_selector(self.REMOVE_THE_RESTRICTION).click()
