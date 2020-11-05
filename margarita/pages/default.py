import urllib.parse


class Page(object):
    BASE_URL = 'https://virusmusic.fun'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urllib.parse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def refresh(self):
        self.driver.refresh()
