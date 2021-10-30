from pages.default import Page

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class DetailsPage(Page):
    TITLE = '.detail-preview__title'

    def get_title(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.TITLE))
        ).text
