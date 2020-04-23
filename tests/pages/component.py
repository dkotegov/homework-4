from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.config import Seed


class Component(Seed):
    def __init__(self, driver):
        self.driver = driver

class FormComponent(Component):
    def fill_input(self, element, value):
        element.click()
        element.clear()
        element.send_keys(value)

    def wait_for_presence(self, method, key, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located((method, key))
        )
        assert element

    def wait_for_visible(self, method, key, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((method, key))
        )
        assert element

    def get_elem_text(self, name):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(name).text
        )

    def get_value_elem_text(self, name):
        return self.driver.find_element_by_xpath(name).get_attribute('value')
