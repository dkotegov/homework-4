
from selenium.webdriver.support.ui import WebDriverWait



class DefaultPage:
    BASE_URL = 'https://ykoya.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = self.BASE_URL + self.PATH
        self.driver.get(url)
        self.driver.maximize_window()
