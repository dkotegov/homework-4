from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait


class AddressForm(Component):
    ADDRESS = '//input[@class="search-field__input-field"]'
    INPUT = '//div[contains(@class,"geo-input__input")]'
    SUBMIT = '//button[@id="geo-popup-submit"]'

    def wait_open(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INPUT).is_displayed()
        )

    def address_form_open(self):
        self.driver.find_element_by_xpath(self.ADDRESS).click()

    def set_address(self, address):
        self.driver.find_element_by_xpath(self.INPUT).send_keys(address)

    def submit(self):
        WebDriverWait(self.driver, 2, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT).is_displayed()
        )
        self.driver.find_element_by_xpath(self.SUBMIT).click()
