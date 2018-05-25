import urllib.parse as urlparse


class Page(object):
    BASE_URL = 'https://ok.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def redirect(self, path):
        url = urlparse.urljoin(self.BASE_URL, path)
        self.driver.get(url)

    def reload(self):
        self.driver.refresh()
