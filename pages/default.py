ROOT_URL = 'https://cinemedia.ru'


class DefaultPage:
    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = ROOT_URL + url

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()


class Component:
    def __init__(self, driver):
        self.driver = driver
