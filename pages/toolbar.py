import time

import urllib.parse as urlparse
from pages.default import Page

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class ToolbarPage(Page):
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

    FILE_BLOCK = 'div[class*="DataListItemThumb__root"]'
    FILE_SELECTED_BLOCK = 'div[class*="DataListItemThumb__root_selected"]'
    DOWNLOAD = 'div[data-name="download"]'

    def click_on_close_notion(self):
        self.driver.find_element_by_css_selector(self.CLOSE_NOTION).click()

    def click_select_all(self):
        self.driver.find_element_by_css_selector(self.SELECT_ALL).click()

    def all_items_selected(self):
        return len(self.driver.find_elements_by_css_selector(self.FILE_BLOCK)) == \
               len(self.driver.find_elements_by_css_selector(self.FILE_SELECTED_BLOCK))

    def click_on_download(self):
        self.driver.find_element_by_css_selector(self.DOWNLOAD).click()


