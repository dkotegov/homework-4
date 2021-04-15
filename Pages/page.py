from urllib.parse import urljoin
import os


class Page(object):
    SIGNUP_LOGIN = os.environ['SIGNUP_LOGIN']
    BASE_URL = 'https://kino-park.online'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
