import urllib.parse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, elem_xpath):
        return self.driver.find_element_by_xpath(elem_xpath)

    def _wait_until_preset(self, elem_xpath):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, elem_xpath)))

    def _wait_until_visible(self, elem_xpath):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, elem_xpath)))

    def _wait_until_invisible(self, elem_xpath):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, elem_xpath)))

    def _wait_until_clickable(self, elem_xpath):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, elem_xpath)))
