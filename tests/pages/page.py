import urllib.parse

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
    BASE_URL = 'https://m.ok.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self, path=None):
        if path is None:
            path = self.PATH

        url = urllib.parse.urljoin(self.BASE_URL, path)
        self.driver.get(url)
        self.driver.maximize_window()

    def refresh(self):
        self.driver.refresh()


class Component(object):
    def __init__(self, driver, element=None):
        self.driver = driver
        self.element = element
        if element is None:
            self.element = self.driver


def wait_until_url_changes(method_to_decorate):
    def wrapper(self):
        url = self.driver.current_url
        method_to_decorate(self)
        WebDriverWait(self.driver, 5).until(EC.url_changes(url))
    return wrapper
