import urllib.parse

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    BASE_URL = 'https://onmeet.ru/'
    PATH = ''

    @classmethod
    def get_default_url(cls):
        return urllib.parse.urljoin(cls.BASE_URL, cls.PATH)

    def __init__(self, driver):
        self.driver = driver

    def open(self, path=None):
        if path is None:
            path = self.PATH
        self.driver.get(urllib.parse.urljoin(self.BASE_URL, path))
        # self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))
