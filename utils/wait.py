from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class Waiter(object):
    @staticmethod
    def wait_clickable_by_xpath(driver, locator):
        delay = 30
        elem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, locator)))
        return elem

    @staticmethod
    def wait_by_xpath(driver, locator, delay=30):
        elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, locator)))
        return elem
