from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseComponent(object):

    def __init__(self, driver):
        self.driver = driver

    def get_clickable_element(self, path):
        return WebDriverWait(self.driver, 8, 0.3)\
            .until(expected_conditions.element_to_be_clickable((By.XPATH, path)))

    def get_visibility_element(self, path):
        return WebDriverWait(self.driver, 8, 0.3) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, path)))

    def get_presence_element(self, path):
        return WebDriverWait(self.driver, 4, 0.3) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, path)))

    def get_searching_element(self, path):
        try:
            WebDriverWait(self.driver, 4, 0.3)\
                .until(expected_conditions.staleness_of(WebDriverWait(self.driver, 4, 0.3)
                                                        .until(expected_conditions.presence_of_element_located((By.XPATH, path)))))
        except TimeoutException:
            return True
        return False
