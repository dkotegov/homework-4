from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait


class AddRestaurantForm(Component):
    INPUT_TITLE = '//input[@id="add-restaurant__name-input"]'
    INPUT_DESCRIPTION = '//textarea[@id="add-restaurant__desc-textarea"]'
    INPUT_PHOTO = '//input[@id="add-restaurant__image-input"]'
    INPUT_ADDRESS = '//div[@id="alone_geo-input__add-rest-point"]'
    INPUT_RADIUS = '//input[@id="add-rest-point__rad-input"]'
    SUBMIT = '//button[contains(@class, "add-restaurant__submit")]'

    TITLE_ERROR = '//div[@id="add-restaurant__name-input-wrapper_err"]'
    DESCRIPTION_ERROR = '//div[@id="add-restaurant__desc-textarea-wrapper_err"]'
    ADDRESS_ERROR = '//div[@id="alone_geo-input__add-rest-point-wrapper_err"]'
    RADIUS_ERROR = '//div[@id="add-rest-point__rad-input-wrapper_err"]'
    PHOTO_ERROR = '//div[@id="img-input__error"]'

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT).is_displayed()
        )

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.INPUT_TITLE).send_keys(title)

    def title_error(self):
        return self.driver.find_element_by_xpath(self.TITLE_ERROR).text

    def title_value(self):
        return self.driver.find_element_by_xpath(self.INPUT_TITLE).text

    def clear_title(self):
        self.driver.find_element_by_xpath(self.INPUT_TITLE).clear()

    def set_description(self, description):
        self.driver.find_element_by_xpath(self.INPUT_DESCRIPTION).send_keys(description)

    def description_error(self):
        return self.driver.find_element_by_xpath(self.DESCRIPTION_ERROR).text

    def clear_description(self):
        self.driver.find_element_by_xpath(self.INPUT_TITLE).clear()

    def set_radius(self, radius):
        self.driver.find_element_by_xpath(self.INPUT_RADIUS).send_keys(radius)

    def radius_error(self):
        return self.driver.find_element_by_xpath(self.RADIUS_ERROR).text

    def radius_value(self):
        return self.driver.find_element_by_xpath(self.INPUT_RADIUS).text
        
    def clear_radius(self):
        self.driver.find_element_by_xpath(self.INPUT_RADIUS).clear()

    def set_address(self, address):
        self.driver.find_element_by_xpath(self.INPUT_ADDRESS).send_keys(address)
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ADDRESS_ERROR).text == '...'
        )
        WebDriverWait(self.driver, 5, 0.1).until_not(
            lambda d: d.find_element_by_xpath(self.ADDRESS_ERROR).text == '...'
        )

    def address_error(self):
        return self.driver.find_element_by_xpath(self.ADDRESS_ERROR).text

    def set_photo(self, path):
        self.driver.find_element_by_xpath(self.INPUT_PHOTO).send_keys(path)

    def photo_error(self):
        return self.driver.find_element_by_xpath(self.PHOTO_ERROR).text

    def submit(self):
        if self.address_error() == '...':
            WebDriverWait(self.driver, 5, 0.1).until_not(
                lambda d: self.address_error() == '...'
            )
        self.driver.find_element_by_xpath(self.SUBMIT).click()