import urllib.parse

from components.navbar import NavBar


class Page(object):
    BASE_URL = 'https://redioteka.com/'
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
