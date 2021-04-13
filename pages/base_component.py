from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Component(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait_time = 15

    def _find_element(self, elem_xpath):
        return self.driver.find_element(By.XPATH, elem_xpath)

    def _find_elements(self, elem_xpath):
        return self.driver.find_elements(By.XPATH, elem_xpath)

    def _wait_until_preset(self, elem_xpath):
        return WebDriverWait(self.driver, self.wait_time ).until(
            EC.presence_of_element_located((By.XPATH, elem_xpath)))

    def _wait_until_visible(self, elem_xpath):
        return WebDriverWait(self.driver, self.wait_time ).until(
            EC.visibility_of_element_located((By.XPATH, elem_xpath)))

    def _wait_until_invisible(self, elem_xpath):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.invisibility_of_element_located((By.XPATH, elem_xpath)))

    def _wait_until_clickable(self, elem_xpath):
        return WebDriverWait(self.driver, self.wait_time ).until(
            EC.element_to_be_clickable((By.XPATH, elem_xpath)))

    def _is_element_visible(self, elem_xpath):
        try:
            return self._find_element(elem_xpath).is_displayed()
        except NoSuchElementException:
            return False
