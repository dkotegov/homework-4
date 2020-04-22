import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Page(object):
    BASE_URL = 'https://solarsunrise.ru'
    PATH = ''
    ROOT = {
        'method': By.ID,
        'key': 'application'
    }

    def __init__(self, driver):
        self.driver = driver

    def open(self, *args):
        url = self.BASE_URL + self.PATH.format(*args)
        print(url + " to open")
        self.driver.get(url)
        self.wait_for_load()
        print(url + " opened")

    def wait_for_presence(self, method, key, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located((method, key))
        )
        assert element

    def wait_for_load(self):
        self.wait_for_presence(self.ROOT['method'], self.ROOT['key'])
