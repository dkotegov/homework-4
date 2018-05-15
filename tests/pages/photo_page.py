from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
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
    LIKE = 'widget_like'
    LIKES_COUNT = 'ecnt'

    @property
    def description(self):
        return self.driver.find_element_by_class_name(self.DESCRIPTION).text

    def like(self):
        widgets = self.driver.find_elements_by_class_name(self.LIKE)
        for widget in widgets:
            try:
                widget.click()
                return
            except ElementClickInterceptedException:
                pass
        raise KeyError

    @property
    def likes_count(self):
        try:
            likes_count = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.LIKES_COUNT))
            )
            return int(likes_count.text)
        except TimeoutException:
            return 0
