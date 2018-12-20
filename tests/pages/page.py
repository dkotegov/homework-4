# coding=utf-8
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from component import Component


class Page(object):
    BASE_URL = 'http://localhost:5007/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver
        self.component = Component(self.driver)

    def open(self):
        url = self.BASE_URL + self.PATH
        self.driver.get(url)
        self.driver.maximize_window()

    def reload(self):
        self.driver.refresh()

    def alert_accept(self):
        alert_text = self.component.alert_accept()
        return alert_text

    def alert_input_and_accept(self, input_int):
        self.component.alert_input_and_accept(input_int)