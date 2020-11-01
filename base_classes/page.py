import urllib.parse

from selenium.webdriver.remote.webdriver import WebDriver

from components.main_header import MainHeader


class Page(object):
    BASE_URL = 'https://drello.works/'
    PATH = ''

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.main_header = MainHeader(driver)

    def open(self):
        url = urllib.parse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
