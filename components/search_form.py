from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class SearchFormLocators:
    def __init__(self):
        self.professionSelector = '//div[@data-test-id="searchJob"]'
        self.searchButton = '//div[@data-test-id="searchBtn"]'


class SearchForm(BaseComponent):
    def __init__(self, driver):
        super(SearchForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = SearchFormLocators()

    def input_profession(self, text: str):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.professionSelector)))
        element.clear()
        element.send_keys(text)

    def click_on_search(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.searchButton)))
        element.click()
