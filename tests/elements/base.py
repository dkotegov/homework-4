# coding=utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement(object):
    locator = None
    DEFAULT_WAIT_TIME = 30

    def __init__(self, driver):
        self.driver = driver
        self.element = WebDriverWait(driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.visibility_of_element_located(self.locator)
        )

    def get(self):
        return self.element
