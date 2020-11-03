from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class AddPointForm(Component):
    ADDRESS = '//div[@id="alone_geo-input__add-rest-point"]'
    ADDRESS_ERROR = '//div[@id="alone_geo-input__add-rest-point-wrapper_err"]'
    RADIUS = '//input[@id="add-rest-point__rad-input"]'
    RADIUS_ERROR = '//div[@id="add-rest-point__rad-input-wrapper_err"]'
    SUBMIT = '//button[@id="add-rest-point__submit"]'

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT).is_displayed()
        )

    def set_address(self, address):
        self.driver.find_element_by_xpath(self.ADDRESS).send_keys(address)
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ADDRESS_ERROR).text == '...'
        )
        WebDriverWait(self.driver, 5, 0.1).until_not(
            lambda d: d.find_element_by_xpath(self.ADDRESS_ERROR).text == '...'
        )

    def address_error(self):
        return self.driver.find_element_by_xpath(self.ADDRESS_ERROR).text

    def set_radius(self, radius):
        self.driver.find_element_by_xpath(self.RADIUS).send_keys(radius)

    def radius_error(self):
        return self.driver.find_element_by_xpath(self.RADIUS_ERROR).text

    def radius_text(self):
        return self.driver.find_element_by_xpath(self.RADIUS).text

    def clean_radius(self):
        self.driver.find_element_by_xpath(self.RADIUS).clear()

    def submit(self):
        WebDriverWait(self.driver, 5, 0.1).until_not(
            lambda d: d.find_element_by_xpath(self.ADDRESS_ERROR).text == '...'
        )
        self.driver.find_element_by_xpath(self.SUBMIT).click()
