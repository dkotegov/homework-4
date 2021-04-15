import urllib.parse
from selenium.webdriver import Remote


class Page(object):
    base_url = ''
    path = ''

    def __init__(self, driver: Remote):
        self.driver = driver

    def open(self):
        url = urllib.parse.urljoin(self.base_url, self.path)
        self.driver.get(url)
        self.driver.maximize_window()
