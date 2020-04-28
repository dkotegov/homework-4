from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

from tests.conftest import accessor


class CustomWebElement(WebElement):
    def __init__(self, element):
        self.element = element

    def click(self):
        accessor.waiter.until(element_to_be_clickable(self.element)).click()
