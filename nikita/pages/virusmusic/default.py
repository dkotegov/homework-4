import urllib.parse

from nikita.constants import VIRUSMUSIC_BASE_URL

class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urllib.parse.urljoin(VIRUSMUSIC_BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def refresh(self):
        self.driver.refresh()
