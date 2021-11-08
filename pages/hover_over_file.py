import time
import os
import urllib.parse as urlparse
from selenium.webdriver.common.action_chains import ActionChains

from pages.default import Page


class HoverOverFilePage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home'

    FAV_SECTION = 'favorites'

    FAV_ICON = 'div[class*="FavoriteIcon"]'
    DOWNLOAD_ICON = 'a[data-qa-id^="/"] svg'

    FILE_NAME = ''

    def add_to_favorites_first_file(self):
        potential_files = self.driver.find_elements_by_css_selector(self.FILES)
        for i in range(len(potential_files)):
            if self.FAV_FILES.count(potential_files[i].get_attribute('data-id')) == 0:
                self.FILE_NAME = potential_files[i].get_attribute('data-id')
                element = self.driver.find_element_by_css_selector('a[data-id="' + potential_files[i].get_attribute('data-id') + '"]')
                fav_icon = self.driver.find_elements_by_css_selector(self.FAV_ICON)[i]
                ActionChains(self.driver).move_to_element(element).click(fav_icon).perform()
                return

    def check_item_in_favorites(self):
        for file_elem in self.driver.find_elements_by_css_selector(self.FILES):
            if file_elem.get_attribute('data-id') == self.FILE_NAME:
                return True
        return False

    def remove_first_file_from_favorites(self):
        potential_files = self.driver.find_elements_by_css_selector(self.FILES)
        for i in range(len(potential_files)):
            if self.FAV_FILES.count(potential_files[i].get_attribute('data-id')) == 1:
                self.FILE_NAME = potential_files[i].get_attribute('data-id')
                element = self.driver.find_element_by_css_selector(
                    'a[data-id="' + potential_files[i].get_attribute('data-id') + '"]')
                fav_icon = self.driver.find_elements_by_css_selector(self.FAV_ICON)[i]
                ActionChains(self.driver).move_to_element(element).click(fav_icon).perform()
                return

    def download_first_file(self):
        first_file = self.driver.find_element_by_css_selector(self.FILES)
        self.FILE_NAME = first_file.get_attribute('data-id')[1:]
        ActionChains(self.driver).move_to_element(first_file).click(self.driver.find_element_by_css_selector(self.DOWNLOAD_ICON)).perform()
        # We need this slip for the download to start
        time.sleep(5)

    def check_file_downloaded(self):
        os.chdir(os.environ.get('DOWNLOAD_FOLDER'))
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        return files.count(self.FILE_NAME) != 0
