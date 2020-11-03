import urllib.parse

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from components.main_header import MainHeader


class Page(object):
    BASE_URL = 'https://drello.works/'
    PATH = ''
    CONTAINER = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.main_header = MainHeader(driver)

    @property
    def url(self):
        return urllib.parse.urljoin(self.BASE_URL, self.PATH)

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        if self.CONTAINER is not None:
            self.wait_for_container()

    def wait_for_container(self):
        if self.CONTAINER is None:
            raise NotImplementedError('CONTAINER is None')

        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CONTAINER)
        )
