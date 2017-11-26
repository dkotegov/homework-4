# -*- coding: utf-8 -*-

import urlparse


class Page(object):
    BASE_URL = 'https://www.ok.ru'

    def __init__(self, driver, path=''):
        self.driver = driver
        self.PATH = path

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
