from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait


class AddRestaurantForm(Component):
    INPUT_TITLE = '//input[@id="add-restaurant__name-input"]'
    INPUT_DESCRIPTION = '//textarea[@id="add-restaurant__desc-textarea"]'
    INPUT_PHOTO = '//input[@id="add-restaurant__image-input"]'
    INPUT_ADDRESS = '//div[@id="alone_geo-input__add-rest-point"]'
    INPUT_RADIUS = '//input[@id="add-rest-point__rad-input"]'
    SUBMIT = '//button[contains(@class, "add-restaurant__submit")]'

    def wait_open(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT).is_displayed()
        )

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.INPUT_TITLE).send_keys(title)

    def set_description(self, description):
        self.driver.find_element_by_xpath(self.INPUT_DESCRIPTION).send_keys(description)

    def set_radius(self, radius):
        self.driver.find_element_by_xpath(self.INPUT_RADIUS).send_keys(radius)

    def set_address(self, address):
        self.driver.find_element_by_xpath(self.INPUT_ADDRESS).send_keys(address)

    def set_photo(self, path):
        self.driver.find_element_by_xpath(self.INPUT_PHOTO).send_keys(path)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()