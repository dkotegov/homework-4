from helpers.helpers import Helpers


class Page(object):
    BASE_URL = "https://ykoya.ru"
    BACK_URL = "/api/v1"
    PATH = ""

    def __init__(self, driver):
        self.driver = driver
        self.helpers = Helpers(driver=driver)

    def change_path(self, path):
        self.PATH = path

    def open(self):
        url = self.BASE_URL + self.PATH
        self.driver.maximize_window()
        self.driver.get(url)

    def wait_page(self):
        raise Exception("release method")

    def is_compare_url(self, url):
        return self.BASE_URL + self.PATH == url
