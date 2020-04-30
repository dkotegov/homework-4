from selenium.webdriver.common.by import By
from tests.pages.config import Seed


class Page(Seed):
    PATH = ''
    ROOT = {
        'method': By.ID,
        'key': 'application'
    }

    def __init__(self, driver):
        self.driver = driver

    def open(self, *args):
        url = self.BASE_URL + self.PATH.format(*args)
        self.driver.get(url)
        self.wait_for_load()

    def wait_for_load(self):
        self.wait_for_presence(self.ROOT['method'], self.ROOT['key'])

    @staticmethod
    def get_xpath_visible(s):
        return s + '[not(contains(@style, "display: none"))]'
