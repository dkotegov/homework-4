import urllib.parse

from selenium.webdriver.remote.webdriver import WebDriver

from components.main_header import MainHeader


class Page(object):
    BASE_URL = 'https://drello.works/'
    PATH = ''

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.main_header = MainHeader(driver)

    @property
    def url(self):
    	return urllib.parse.urljoin(self.BASE_URL, self.PATH)

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
