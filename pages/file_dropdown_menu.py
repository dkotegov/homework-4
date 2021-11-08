import time
import os
import urllib.parse as urlparse
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from pages.default import Page


class FileDropDownMenuPage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home'

    FAV_SECTION = 'favorites'
    BIN_SECTION = 'trashbin'
    SELECTED_FILE_NAME = ''
    FILES = 'a[data-id^="/"]'
    NEW_TAB = 'div[data-name="newTab"]'
    SEND_VIA_MAIL = 'div[data-name="sendViaMail"]'
    ADD_TO_FAVORITE = 'div[data-name="addToFavorite"]'
    RENAME = 'div[data-name="rename"]'
    DOWNLOAD = 'div[data-name="download"]'
    REMOVE = 'div[data-name="remove"]'
    OPENED_NEW_TAB_FILE_NAME = 'div[class*="ViewerHeader__fileName"]'
    ATTACHED_TO_MAIL_FILE_NAME = 'div[message-uid] span[title]:not(.button2)'
    INPUT_FILE_NAME = 'div[data-qa-modal] input'
    SUBMIT = 'div[data-qa-modal] button[class*="primary"]'
    ERROR_RENAME = 'div[class*="index__error"]'
    CLOSE_MODAL = 'div[class*="Dialog__close"]'
    MODAL_REMOVE = 'div[data-qa-modal="remove-confirmation-dialog"]'

    def right_click_first_file(self):
        self.SELECTED_FILE_NAME = self.driver.find_element_by_css_selector(self.FILES).get_attribute('data-id')[1:]
        first_file = self.driver.find_element_by_css_selector(self.FILES)
        ActionChains(self.driver).context_click(first_file).perform()

    def open_in_new_tab(self):
        self.driver.find_element_by_css_selector(self.NEW_TAB).click()

    def send_via_male(self):
        self.driver.find_element_by_css_selector(self.SEND_VIA_MAIL).click()

    def right_click_on_non_fav_item(self):
        potential_files = self.driver.find_elements_by_css_selector(self.FILES)
        for i in range(len(potential_files)):
            if self.FAV_FILES.count(potential_files[i].get_attribute('data-id')) == 0:
                self.SELECTED_FILE_NAME = potential_files[i].get_attribute('data-id')
                ActionChains(self.driver).context_click(potential_files[i]).perform()
                return

    def click_add_to_favorites(self):
        self.driver.find_element_by_css_selector(self.ADD_TO_FAVORITE).click()

    def check_item_in_favorites(self):
        for file_elem in self.driver.find_elements_by_css_selector(self.FILES):
            if file_elem.get_attribute('data-id') == self.SELECTED_FILE_NAME:
                return True
        return False

    def click_rename(self):
        self.driver.find_element_by_css_selector(self.RENAME).click()

    def remove_rename_input(self):
        self.driver.find_element_by_css_selector(self.INPUT_FILE_NAME).send_keys(Keys.BACKSPACE)

    def input_long_string(self):
        res_string = ''
        for i in range(322):
            res_string += 'a'
        self.driver.find_element_by_css_selector(self.INPUT_FILE_NAME).send_keys(res_string)

    def click_submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()

    def click_download(self):
        self.driver.find_element_by_css_selector(self.DOWNLOAD).click()
        # We need this slip for the download to start
        time.sleep(5)

    def click_remove(self):
        self.driver.find_element_by_css_selector(self.REMOVE).click()

    def close_modal_remove(self):
        self.driver.find_element_by_css_selector(self.CLOSE_MODAL).click()

    def check_file_in_bin(self):
        for removed_file in self.driver.find_elements_by_css_selector(self.FILES):
            if removed_file.get_attribute('data-qa-name') == self.SELECTED_FILE_NAME:
                return True
        return False

    def check_remove_modal_exists(self):
        try:
            self.driver.find_element_by_css_selector(self.MODAL_REMOVE)
            return True
        except Exception:
            return False

    def check_error_exists(self):
        try:
            self.driver.find_element_by_css_selector(self.SUBMIT)
            return True
        except Exception:
            return False

    def check_file_downloaded(self):
        os.chdir(os.environ.get('DOWNLOAD_FOLDER'))
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        return files.count(self.SELECTED_FILE_NAME) != 0

    def compare_file_names(self, selector):
        return self.driver.find_element_by_css_selector(selector).text == self.SELECTED_FILE_NAME

