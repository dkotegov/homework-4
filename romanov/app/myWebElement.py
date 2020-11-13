from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class wait_for_the_attribute_value(object):
    def __init__(self, locator, attribute, value=None):
        self.locator = locator
        self.attribute = attribute
        self.value = value

    def __call__(self, driver):
        try:
            element_attribute = EC._find_element(driver, self.locator).get_attribute(self.attribute)
            return (element_attribute == self.value and self.value is not None)\
                or (element_attribute is not None and self.value is None)
        except StaleElementReferenceException:
            return False

class MyWebElement:
    def __init__(self, el: WebElement, id=None, css=None, xpath=None):
        self.el: WebElement = el
        self.id = id
        self.css = css
        self.xpath = xpath

    def click(self):
        self.el.click()

    def input(self, keys):
        self.el.send_keys(keys)

    def click_after_wait(self):
        from romanov.app.driver import connect
        if self.id:
            connect.wait.until(element_to_be_clickable((By.ID, self.id))).click()
        elif self.css:
            connect.wait.until(element_to_be_clickable((By.CSS_SELECTOR, self.css))).click()
        else:
            connect.wait.until(element_to_be_clickable((By.XPATH, self.xpath))).click()

    def change_wait(self, key, value=None):
        from romanov.app.driver import connect
        if self.id:
            connect.wait.until(wait_for_the_attribute_value((By.ID, self.id), key, value))
        elif self.css:
            connect.wait.until(wait_for_the_attribute_value((By.CSS_SELECTOR, self.css), key, value))

