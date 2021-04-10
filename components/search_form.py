from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class SearchFormLocators:
    def __init__(self):
        self.profession_selector = '//input[@id="searchJob"]'
        self.search_button = '//div[@id="searchBtn"]'
        self.place_selector = '//input[@id="searchPlace"]'


class SearchForm(BaseComponent):
    def __init__(self, driver):
        super(SearchForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = SearchFormLocators()

    def input_profession(self, profession: str) -> None:
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.profession_selector)))
        element.clear()
        element.send_keys(profession)

    def click_on_search(self) -> None:
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.search_button)))
        element.click()

    def input_place(self, place: str) -> None:
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.place_selector)))
        element.clear()
        element.send_keys(place)

