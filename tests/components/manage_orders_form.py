from tests.components.component import Component

from selenium.webdriver.support.wait import WebDriverWait


class ManageOrdersForm(Component):
    LIST = '//main[@class="restaurants-list-view"]'
    ORDERS = '//div[contains(@class, "restaurant-item")]'
    STATUS = './/div[@class="order-item__name"]'
    CHANGE_BUTTON = '//button[@id="order-item{}__button"]'
    MESSAGE = '//div[@id="message"]'

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.3).until(
            lambda d: d.find_element_by_xpath(self.ORDERS)
        )

    def status(self, num):
        return self.driver.find_element_by_xpath(self.STATUS).text

    def change_status(self, num):
        id = self.driver.find_elements_by_xpath(self.ORDERS)[num].get_attribute('id')
        self.driver.find_elements_by_xpath(self.ORDERS)[num].click()
        WebDriverWait(self.driver, 5, 0.3).until(
            lambda d: d.find_element_by_xpath(self.CHANGE_BUTTON.format(id))
        )
        self.driver.find_element_by_xpath(self.CHANGE_BUTTON.format(id)).click()

    def message(self):
        return self.driver.find_element_by_xpath(self.MESSAGE).text
