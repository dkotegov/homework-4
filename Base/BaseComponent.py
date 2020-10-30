from typing import List

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Component(object):
    def __init__(self, driver: Remote):
        self.driver = driver

    def _wait_until_and_get_elem_by_xpath(self, elem) -> WebElement:
        return WebDriverWait(self.driver, 30, 0.1).until(EC.visibility_of_element_located((By.XPATH, elem)))

    def _wait_until_and_get_elem_by_css(self, elem) -> WebElement:
        return WebDriverWait(self.driver, 30, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elem)))

    def _wait_for_url(self, url):
        return WebDriverWait(self.driver, 30, 0.1).until(EC.url_to_be(url))

    def _check_if_element_exists_by_xpath(self, elem) -> bool:
        try:
            WebDriverWait(self.driver, 1, 0.1).until(EC.visibility_of_all_elements_located((By.XPATH, elem)))
        except TimeoutException:
            return False
        return True
