import time

import urllib.parse as urlparse
from pages.default import Page


class CreateNewFilePage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home'

    CREATE_NEW = 'div[class*="DataListItemCreateNew"]'
    CREATE_NEW_DOC = 'div[data-name="createDoc"]'
    WHITE_LINE = 'div[data-testid="whiteline"]'
    CREATE_NEW_TABLE = 'div[data-name="createCell"]'
    CREATE_NEW_PRES = 'div[data-name="createPpt"]'


    # ALL_FILES = 'div[data-name = "/"]'
    # CREATE_FOLDER = 'div[data-name = "/${process.env.CREATE_FOLDER}"]'

    def click_on_create_new(self):
        self.driver.find_element_by_css_selector(self.CREATE_NEW).click()

    def click_on_create_new_doc(self):
        self.driver.find_element_by_css_selector(self.CREATE_NEW_DOC).click()

    def click_on_create_new_table(self):
        self.driver.find_element_by_css_selector(self.CREATE_NEW_TABLE).click()

    def click_on_create_new_pres(self):
        self.driver.find_element_by_css_selector(self.CREATE_NEW_PRES).click()
