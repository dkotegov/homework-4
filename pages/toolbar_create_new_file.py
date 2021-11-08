import time
import os
import urllib.parse as urlparse
from selenium.webdriver.common.action_chains import ActionChains

from pages.default import Page


class ToolbarCreateNewFilePage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home'

    CREATE = 'div[data-name="create"]'
    FOLDER = 'div[data-name="createFolder"]'
    DOCX = 'div[data-name="createDocx"]'
    TABLE = 'div[data-name="createXlsx"]'
    PRESENTATION = 'div[data-name="createPptx"]'
    MODAL = 'div[data-qa-modal]'

    def click_create(self):
        self.driver.find_element_by_css_selector(self.CREATE).click()

    def click_folder(self):
        self.driver.find_element_by_css_selector(self.FOLDER).click()

    def click_docx(self):
        self.driver.find_element_by_css_selector(self.DOCX).click()

    def click_table(self):
        self.driver.find_element_by_css_selector(self.TABLE).click()

    def click_presentation(self):
        self.driver.find_element_by_css_selector(self.PRESENTATION).click()

    def check_modal_exists(self):
        try:
            self.driver.find_element_by_css_selector(self.MODAL)
            return True
        except Exception:
            return False

