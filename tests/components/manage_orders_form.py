from tests.components.component import Component

from selenium.webdriver.support.wait import WebDriverWait

class ManageOrdersForm(Component):
    ORDER = '//div[@id="{}" and contains(@class, "restaurant-item")]'
    ORDERS = '//div[contains(@class, "restaurant-item")]'
    STATUS = './/div[@class="order-item__name"]'
    CHANGE_BUTTON = '//button[@id="order-item{}__button"]'
    MESSAGE = '//div[@class="message restaurant-list-view__message"]'

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ORDERS).is_displayed()
        )

    def get_order_id(self, num):
        return self.driver.find_elements_by_xpath(self.ORDERS)[num].get_attribute('id')

    def status(self, order_id):
        return self.driver.find_element_by_xpath(self.ORDER.format(order_id)).find_element_by_xpath(self.STATUS).text

    def change_status(self, order_id):
        self.driver.find_element_by_xpath(self.ORDER.format(order_id)).click()
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHANGE_BUTTON.format(order_id)).is_displayed()
        )
        self.driver.find_element_by_xpath(self.CHANGE_BUTTON.format(order_id)).click()

    def message(self):
        return self.driver.find_element_by_xpath(self.MESSAGE).text
