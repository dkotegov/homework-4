from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class SearchFormLocators:
    def __init__(self):
        self.professionSelector = '//input[@id="searchJob"]'
        self.searchButton = '//div[@id="searchBtn"]'
        self.placeSelector = '//input[@id="searchPlace"]'


class SearchForm(BaseComponent):
    def __init__(self, driver):
        super(SearchForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = SearchFormLocators()

    def input_profession(self, proffesion: str) -> None:
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.professionSelector)))
        element.clear()
        element.send_keys(proffesion)

    def click_on_search(self) -> None:
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.searchButton)))
        element.click()

    def input_place(self, place: str) -> None:
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.placeSelector)))
        element.clear()
        element.send_keys(place)
