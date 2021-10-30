from pages.default import Page

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class GenrePage(Page):
    GENRE_NAME = '.item__page-title'

    def get_genre_name(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.GENRE_NAME))
        ).text

