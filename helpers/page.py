from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers.helpers import Helpers


class Page(object):
    BASE_URL = "https://ykoya.ru"
    BACK_URL = "/api/v1"
    PATH = ""

    def __init__(self, driver):
        self.driver = driver
        self.helpers = Helpers(driver=driver)

    def __wait_page__(self, selector):
        self.helpers.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def change_path(self, path):
        self.PATH = path

    def open(self, wait=True):
        url = self.BASE_URL + self.PATH
        self.driver.maximize_window()
        self.driver.get(url)

        if wait:
            self.wait_page()

    def wait_page(self):
        raise Exception("release method")

    def is_compare_url(self, url):
        return self.BASE_URL + self.PATH == url
