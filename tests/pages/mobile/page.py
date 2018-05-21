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

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def refresh(self):
        self.driver.refresh()

    @property
    def current_url(self):
        return self.driver.current_url


class Component(object):
    def __init__(self, driver, element=None):
        self.driver = driver
        self.element = element
        if element is None:
            self.element = self.driver
