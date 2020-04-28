from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable


class CustomWebElement:
    def __init__(self, element: WebElement, css_locator=""):
        self.element: WebElement = element
        self.css_locator = css_locator

    def click(self):
        self.element.click()

    def wait_and_click(self):
        from tests.conftest import accessor
        accessor.waiter.until(element_to_be_clickable((By.CSS_SELECTOR, self.css_locator))).click()
