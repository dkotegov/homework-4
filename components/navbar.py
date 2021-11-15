from components.component import Component
from selenium.common.exceptions import NoSuchElementException


class NavbarComponent(Component):
    USERNAME = '//h3[@id="navbar-username"]'
    RESTAURANT_NAME = '//h3[@id="navbar-username"]'
    ADDRESS_COMPONENT = '//button[@id="address"]'

    def check_if_customer_logged(self):
        try:
            self.driver.find_element_by_xpath(self.USERNAME)
        except NoSuchElementException:
            return False
        return True

    def check_if_restaurant_logged(self):
        try:
            self.driver.find_element_by_xpath(self.RESTAURANT_NAME)
        except NoSuchElementException:
            return False
        return True

    def get_username(self):
        return self.driver.find_element_by_xpath(self.USERNAME).text

    def click_address(self):
        self.driver.find_element_by_xpath(self.ADDRESS_COMPONENT).click()
