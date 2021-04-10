from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent


class KeySearchFormLocators:
    def __init__(self):
        self.root = '//div[@class="main-search-form"]'
        self.keyword_selector = '//input[@id="keywords-search__input"]'
        self.search_button = '//div[@class="main-search-form__btn"]'


class KeySearchForm(BaseComponent):
    def __init__(self, driver):
        super(KeySearchForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = KeySearchFormLocators()

    def input_keyword(self, key: str) -> None:
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.keyword_selector)))
        element.clear()
        element.send_keys(key)

    def click_on_search(self) -> None:
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.search_button)))
        element.click()


