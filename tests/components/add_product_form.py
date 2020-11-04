from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait


class AddProductForm(Component):
    TITLE = '//input[@id="add-product-by-restaurant__name-input"]'
    TITLE_ERROR = '//div[@id="add-product-by-restaurant__name-input-wrapper_err"]'
    PRICE = '//input[@id="add-product-by-restaurant__cost-input"]'
    PRICE_ERROR = '//div[@id="add-product-by-restaurant__cost-input-wrapper_err"]'
    PHOTO = '//input[@id="add-product__image-input"]'
    PHOTO_ERROR = '//div[@id="add-product__image-input-wrapper_err"]'
    SUBMIT = '//button[contains(@class, "add-product-by-restaurant__submit")]'

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT).is_displayed()
        )

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)
    
    def title_error(self):
        return self.driver.find_element_by_xpath(self.TITLE_ERROR).text

    def clear_title(self):
        self.driver.find_element_by_xpath(self.TITLE).clear()

    def title_value(self):
        return self.driver.find_element_by_xpath(self.TITLE).text

    def set_price(self, price):
        self.driver.find_element_by_xpath(self.PRICE).send_keys(price)
    
    def price_error(self):
        return self.driver.find_element_by_xpath(self.PRICE_ERROR).text

    def clear_price(self):
        self.driver.find_element_by_xpath(self.PRICE).clear()

    def price_value(self):
        return self.driver.find_element_by_xpath(self.PRICE).text

    def set_photo(self, photo_path):
        self.driver.find_element_by_xpath(self.PHOTO).send_keys(photo_path)
    
    def photo_error(self):
        return self.driver.find_element_by_xpath(self.PHOTO_ERROR).text

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
