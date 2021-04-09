import urllib.parse


class BasePage(object):
    BASE_URL = 'https://studhunt.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        url = urllib.parse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
