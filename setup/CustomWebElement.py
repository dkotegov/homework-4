from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located


class CustomWebElement:
    def __init__(self, element: WebElement, id_locator=None, css_locator=None):
        self.element: WebElement = element
        self.id_locator = id_locator
        self.css_locator = css_locator

    def click(self):
        self.element.click()

    def send_keys(self, keys: str):
        self.element.send_keys(keys)

    def get_text(self):
        return self.element.text

    def wait_and_click(self):
        from tests.conftest import accessor
        if self.id_locator is not None:
            accessor.waiter.until(element_to_be_clickable((By.ID, self.id_locator))).click()
        elif self.css_locator:
            accessor.waiter.until(element_to_be_clickable((By.CSS_SELECTOR, self.css_locator))).click()
