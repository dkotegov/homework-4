from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseComponent(object):

    def __init__(self, driver):
        self.driver = driver

    def get_clickable_element(self, path):
        return WebDriverWait(self.driver, 10, 0.2)\
            .until(expected_conditions.element_to_be_clickable((By.XPATH, path)))

    def get_visibility_element(self, path):
        return WebDriverWait(self.driver, 10, 0.2) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, path)))

    def get_visibility_elements(self, path):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_elements_by_xpath(path)
        )
