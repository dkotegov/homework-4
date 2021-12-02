import urllib.parse

import constants
from components.navbar import NavBar


class Page(object):
    BASE_URL = constants.REDIOTEKA_BASE_URL
    PATH = ''

    def __init__(self, driver):
        self.driver = driver
        self.navbar = None

    def open(self):
        url = urllib.parse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def set_navbar(self):
        self.navbar = NavBar(self.driver)
