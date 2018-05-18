import urlparse

from selenium import webdriver
from selenium.webdriver import ActionChains


class Page(object):
    BASE_URL = 'https://ok.ru'
    PAGE = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PAGE)
        self.driver.get(url)
        self.driver.maximize_window()

    def get_hover(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

