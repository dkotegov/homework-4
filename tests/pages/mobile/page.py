import urllib.parse

from selenium.common.exceptions import NoSuchElementException


class Page(object):
    BASE_URL = 'https://m.ok.ru/'
    PATH = ''
    TOUCH_OVERLAY = 'touch-overlay'

    def __init__(self, driver):
        self.driver = driver

    def open(self, path=None):
        if path is None:
            path = self.PATH

        url = urllib.parse.urljoin(self.BASE_URL, path)
        self.driver.get(url)
        self.driver.maximize_window()

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def refresh(self):
        self.driver.refresh()

    @property
    def current_url(self):
        return self.driver.current_url

    @property
    def is_xss(self):
        try:
            return self.driver.find_element_by_id('xss')
        except NoSuchElementException:
            return False

    def touch_overlay(self):
        try:
            self.driver.find_element_by_class_name(self.TOUCH_OVERLAY).click()
        except NoSuchElementException:
            pass


class Component(object):
    def __init__(self, driver):
        self.driver = driver
