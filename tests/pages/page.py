import urllib.parse


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


class Component(object):
    def __init__(self, driver):
        self.driver = driver
