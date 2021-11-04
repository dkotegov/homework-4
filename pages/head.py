import time

import urllib.parse as urlparse
from pages.default import Page

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class HeadPage(Page):
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

    SELECT_ALL = 'div[data-name="selectAll"]'

    FILE_BLOCK = 'div[class*="DataListItemThumb__root"]'
    FILE_SELECTED_BLOCK = 'div[class*="DataListItemThumb__root_selected"]'

    LOGO = 'a[class*="pm-logo__link"]'
    HELP = 'span[data-icon="ph-icons-video-help"]'

    def click_on_close_notion(self):
        self.driver.find_element_by_css_selector(self.CLOSE_NOTION).click()

    def click_on_logo(self):
        self.driver.find_element_by_css_selector(self.LOGO).click()

    def click_on_help(self):
        self.driver.find_element_by_css_selector(self.HELP).click()
