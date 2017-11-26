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

    def wait_for_clickable(self):
        self.element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.element_to_be_clickable(self.locator)
        )
        return self

    def wait_for_alert(self):
        self.element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.alert_is_present()
        )
        return self

    def is_exists(self):
        try:
            self.driver.find_element(self.locator)
        except Exception as e:
            return False
        return True

    def get(self):
        return self.element

    def __getattr__(self, item):
        def f():
            self.locator = self.__getattribute__(item.upper())
            return self
        return f
