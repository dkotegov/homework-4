from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from enum import Enum


class SELECTOR(Enum):
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH


class Helpers:
    def __init__(self, driver):
        self.driver = driver
        self.SELECTOR = SELECTOR

    def wait(self, until, who=None, timeout=30, step=0.1):
        if who is None:
            who = self.driver
        return WebDriverWait(who, timeout, step).until(until)

    def __get_selenium_by__(self, by):
        if by == SELECTOR.CSS:
            return By.CSS_SELECTOR
        elif by == SELECTOR.XPATH:
            return By.XPATH

        raise Exception("wrong by")

    def __find_element__(self, selector, by, wait):
        if wait:
            self.wait(until=EC.presence_of_element_located((by, selector)))
        return self.driver.find_element(by, selector)

    def __find_elements__(self, selector, by, wait):
        if wait:
            self.wait(until=EC.presence_of_element_located((by, selector)))
        return self.driver.find_elements(by, selector)

    def get_element(self, selector, by=SELECTOR.CSS, wait=True):
        return self.__find_element__(selector, self.__get_selenium_by__(by), wait)

    def get_elements(self, selector, by=SELECTOR.CSS, wait=True):
        return self.__find_elements__(selector, self.__get_selenium_by__(by), wait)

    def click_element(self, selector, by=SELECTOR.CSS):
        self.wait(until=EC.element_to_be_clickable((self.__get_selenium_by__(by), selector)))
        element = self.get_element(selector, by)
        element.click()

    def input_value(self, selector, value, by=SELECTOR.CSS):
        element = self.get_element(selector, by)
        element.send_keys(value)

    def clear_input(self, selector, by=SELECTOR.CSS):
        element = self.get_element(selector, by)
        element.clear()

    def enter(self, selector, by=SELECTOR.CSS):
        element = self.get_element(selector, by)
        element.send_keys(Keys.ENTER)

    def upload_file(self, selector, file_path, by=SELECTOR.CSS):
        element = self.get_element(selector, by)
        element.send_keys(file_path)

    def is_contains(self, selector, by=SELECTOR.CSS):
        try:
            return self.get_element(selector, by, wait=False) is not None
        except NoSuchElementException:
            return False

    def is_element_contains_class(self, element, search_class):
        return element.get_attribute("class").find(search_class) != -1

    def is_contains_class(self, selector, search_class, by=SELECTOR.CSS):
        element = self.get_element(selector, by)
        return self.is_element_contains_class(element, search_class)

    def fetch(self, url, method="POST"):
        fetch = "fetch(\"{}\", ".format(url) + "{\"method\": " + "\"{}\"".format(method) + "})"
        self.driver.execute_script(fetch)
