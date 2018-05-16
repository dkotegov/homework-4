from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseComponent(object):

    def __init__(self, driver):
        self.driver = driver

    # def get_element_1(self, path):
    #     return WebDriverWait(self.driver, 10, 0.2)\
    #         .until(expected_conditions.element_to_be_clickable((By.XPATH, path)))