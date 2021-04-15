from testutils import Component
from selenium.webdriver.common.by import By


class Converter(Component):
    container = '[data-test-id=modal]'

    class Selectors:
        first_field = 'input[id="leftCurrency"]'
        second_field = 'input[id="rightCurrency"]'
        converter_icon = 'img[alt="calculator"]'

    def fill_first_field(self, value):
        self.driver.find_element_by_id("leftCurrency").clear()
        self._fill_input(By.CSS_SELECTOR, self.Selectors.first_field, value)

    def fill_second_field(self, value):
        self.driver.find_element_by_id("rightCurrency").clear()
        self._fill_input(By.CSS_SELECTOR, self.Selectors.second_field, value)

    def open_converter(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.converter_icon).click()

    def get_first_form_content(self) -> str:
        return self.driver.find_element_by_id("leftCurrency").get_attribute("value")

    def get_second_form_content(self) -> str:
        return self.driver.find_element_by_id("rightCurrency").get_attribute("value")
