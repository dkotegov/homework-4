from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Component(object):
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
