from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AddressForm(Component):
    ADDRESS = '//input[@class="search-field__input-field"]'
    INPUT = '//div[@id="alone_geo-input"]'
    SUBMIT = '//button[@id="geo-popup-submit"]'
    INPUT_ERROR = '//div[@id="alone_geo-input-wrapper_err"]'
    HELP_BLOCK = '//ymaps[@class="ymaps-2-1-77-search__suggest ymaps-2-1-77-popup ymaps-2-1-77-popup_theme_ffffff ymaps-2-1-77-i-custom-scroll"]'

    def wait_open(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INPUT).is_displayed()
        )

    def address_form_open(self):
        self.driver.find_element_by_xpath(self.ADDRESS).click()

    def set_address(self, address):
        self.driver.find_element_by_xpath(self.INPUT).send_keys(address)

    def wait_help_block(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.HELP_BLOCK).is_displayed()
        )

    def get_input_error(self):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INPUT_ERROR).text != ''
                      and
                      d.find_element_by_xpath(self.INPUT_ERROR).text != '...'
        )
        return self.driver.find_element_by_xpath(self.INPUT_ERROR).text

    def submit(self):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT).is_displayed()
        )
        self.driver.find_element_by_xpath(self.SUBMIT).send_keys(Keys.ENTER)
