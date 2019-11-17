from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    BASE_URL = 'https://calendar.mail.ru/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()


class Component(object):
    WAIT_TIME = 15
    FREQ = 0.1

    def __init__(self, driver):
        self.driver = driver

    def wait_for_stale(self, xpath):
        try:
            el = self.driver.find_element_by_xpath(xpath)
            WebDriverWait(self.driver, self.WAIT_TIME, self.FREQ).until(
                EC.staleness_of(el)
            )
        except TimeoutException:
            print('cant find element: ' + xpath)
            return 'Not found'

    def wait_for_visible(self, xpath):
        try:
            element = WebDriverWait(self.driver, self.WAIT_TIME, self.FREQ).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
        except TimeoutException:
            print('cant find element: ' + xpath)
            return 'Not found'
        return element

    def wait_for(self, xpath):
        try:
            element = WebDriverWait(self.driver, self.WAIT_TIME, self.FREQ).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except TimeoutException:
            print('cant find element: ' + xpath)
            return 'Not found'
        return element