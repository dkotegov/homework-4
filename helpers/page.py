from helpers.helpers import Helpers


class Page(object):
    BASE_URL = 'https://ykoya.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver
        self.helpers = Helpers(driver=driver)

    def change_path(self, path):
        self.PATH = path

    def open(self):
        url = self.BASE_URL + self.PATH
        self.driver.maximize_window()
        self.driver.get(url)

    def is_compare_url(self, url):
        return self.BASE_URL + self.PATH == url
