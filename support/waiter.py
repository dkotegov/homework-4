from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class ElementWaiter(object):

    @staticmethod
    def wait(driver, by, locator):
        try:
            delay = 30
            elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((by, locator)))
            print "Page is ready!"
            return elem
        except TimeoutException:
            print "Loading took too much time! Locator is " + locator
            return None

    @staticmethod
    def wait_by_xpath(driver, locator):
        try:
            delay = 30
            elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, locator)))
            print "Page is ready!"
            return elem
        except TimeoutException:
            print "Loading took too much time! Locator is " + locator
            return None

    @staticmethod
    def wait_elements_by_xpath(driver, locator):
        try:
            delay = 30
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, locator)))
            elem = driver.find_elements_by_xpath(locator)
            print "Page is ready!"
            return elem
        except TimeoutException:
            print "Loading took too much time! Locator is " + locator
            return None

    @staticmethod
    def wait_clickable_by_xpath(driver, locator):
        try:
            delay = 30
            elem = WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, locator)))
            print "Page is ready!"
            return elem
        except TimeoutException:
            print "Loading took too much time! Locator is " + locator
            return None