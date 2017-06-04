# coding=utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement(object):
    locator = None
    element = None
    DEFAULT_WAIT_TIME = 30

    def __init__(self, driver):
        self.driver = driver

    def wait_for_presence(self):
        self.element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.presence_of_element_located(self.locator)
        )
        return self

    def wait_for_visible(self):
        self.element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.visibility_of_element_located(self.locator)
        )
        return self

    def is_existed(self):
        try:
            self.driver.find_element(self.locator)
        except Exception as e:
            return False
        return True

    def get(self):
        return self.element

    def get_value(self):
        return self.element.get_attribute('value')