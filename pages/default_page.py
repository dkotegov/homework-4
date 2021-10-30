from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from enum import Enum


class SELECTOR(Enum):
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH


class DefaultPage:
    BASE_URL = 'https://ykoya.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def change_path(self, path):
        self.PATH = path

    def open(self):
        url = self.BASE_URL + self.PATH
        self.driver.maximize_window()
        self.driver.get(url)

    def wait(self, until, who=None, timeout=30, step=0.1):
        if who is None:
            who = self.driver
        return WebDriverWait(who, timeout, step).until(until)

    def is_contains(self, selector, by=SELECTOR.CSS):
        try:
            return self.__get_element__(selector, by, wait=False) is not None
        except NoSuchElementException:
            return False

    def is_compare_url(self, url, **kwargs):
        print(url)
        print(self.BASE_URL + self.PATH)
        return self.BASE_URL + self.PATH == url

    def __contains_class__(self, element, search_class):
        return element.get_attribute("class").find(search_class) != -1

    def __get_element_css__(self, selector, wait=True):
        if wait:
            self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def __get_element_xpath__(self, xpath, wait=True):
        if wait:
            self.wait(until=EC.element_to_be_clickable((By.XPATH, xpath)))
        return self.driver.find_element(By.XPATH, xpath)

    def __get_element__(self, selector, by=SELECTOR.CSS, wait=True):
        if by == SELECTOR.CSS:
            return self.__get_element_css__(selector, wait)
        elif by == SELECTOR.XPATH:
            return self.__get_element_xpath__(selector, wait)

    def __get_elements_css__(self, selector, wait=True):
        if wait:
            self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        return self.driver.find_elements(By.CSS_SELECTOR, selector)

    def __get_elements_xpath__(self, xpath, wait=True):
        if wait:
            self.wait(until=EC.element_to_be_clickable((By.XPATH, xpath)))
        return self.driver.find_elements(By.XPATH, xpath)

    def __get_elements__(self, selector, by=SELECTOR.CSS, wait=True):
        if by == SELECTOR.CSS:
            return self.__get_elements_css__(selector, wait)
        elif by == SELECTOR.XPATH:
            return self.__get_elements_xpath__(selector, wait)

    def __click_button__(self, selector, by=SELECTOR.CSS):
        element = self.__get_element__(selector, by)
        element.click()

    def __input_value__(self, selector, value, by=SELECTOR.CSS):
        element = self.__get_element__(selector, by)
        element.send_keys(value)

    def __clear_input__(self, selector, by=SELECTOR.CSS):
        element = self.__get_element__(selector, by)
        element.clear()

    def __enter__(self, selector, by=SELECTOR.CSS):
        element = self.__get_element__(selector, by)
        element.send_keys(Keys.ENTER)

    def __element_contains_class__(self, selector, search_class, by=SELECTOR.CSS):
        element = self.__get_element__(selector, by)
        return self.__contains_class__(element, search_class)
