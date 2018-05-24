from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import game



class BaseComponent(object):

    def __init__(self, driver):
        self.driver = driver

    def get_clickable_element(self, path):
        return WebDriverWait(self.driver, 10, 0.3)\
            .until(expected_conditions.element_to_be_clickable((By.XPATH, path)))

    def get_clickable_element_by_element(self, element):
        return WebDriverWait(self.driver, 30, 0.3)\
            .until(expected_conditions.element_to_be_clickable(element))

    def get_visibility_element(self, path):
        return WebDriverWait(self.driver, 6, 0.3) \
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

    def trying(self, path):
        return WebDriverWait(self.driver, 4, 0.3).\
            until(expected_conditions.staleness_of((By.XPATH, path)))

    def get_element_by_path(self, path):
        return WebDriverWait(self.driver, 5, 0.2).until(
            lambda d: d.find_element_by_xpath(path)
        )

    def get_elements_by_path(self, path):
        return WebDriverWait(self.driver, 5, 0.2).until(
            lambda d: d.find_elements_by_xpath(path)
        )

    def get_element_by_path_with_exception(self, path):
        try:
            return WebDriverWait(self.driver, 5, 0.2).until(
                lambda d: d.find_element_by_xpath(path)
            )
        except TimeoutException:
            return False

    def get_visibility_element_with_exception(self, path):
        try:
            return WebDriverWait(self.driver, 6, 0.3) \
                .until(expected_conditions.visibility_of_element_located((By.XPATH, path)))
        except TimeoutException:
            return False

    def get_element_by_app(self, id):
        try:
            return self.get_clickable_element(id)
        except TimeoutException:
            return False

    def get_clickable_element_with_exception(self, path):
        try:
            return WebDriverWait(self.driver, 6, 0.3)\
                .until(expected_conditions.element_to_be_clickable((By.XPATH, path)))
        except TimeoutException:
            return False

    def get_visibility_elements(self, path):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_elements_by_xpath(path)
        )       