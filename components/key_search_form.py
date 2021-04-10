from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent


class KeySearchFormLocators:
    def __init__(self):
        self.root = '//div[@class="main-search-form"]'
        self.keyword_selector = '//input[@class="keywords-search__input"]'
        self.search_button = '//button[@class="main-search-form__btn"]'
        self.search_check_box = '//div[@class="option-type"]'
        self.search_check_box_input = 'option-type__checkbox'
        self.search_check_box_name = 'option-type__name'


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

    def click_on_search_checkbox(self) -> str:
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.search_check_box)))

        checkBoxInput = element.find_element_by_class_name(self.locators.search_check_box_input)
        checkBoxInput.click()
        checkBoxName = element.find_element_by_class_name(self.locators.search_check_box_name)
        return checkBoxName.get_attribute('innerText')
