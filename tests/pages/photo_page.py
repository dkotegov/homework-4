from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page, Component


class PhotoPage(Page):
    PATH = ''

    @property
    def photo(self):
        return Photo(self.driver)


class Photo(Component):
    DESCRIPTION = 'photo-description'

    @property
    def description(self):
        return WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.DESCRIPTION))
        ).text
