class DefaultPage:
    ROOT_URL = 'https://cinemedia.ru'

    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = self.ROOT_URL + url

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def reload(self):
        self.driver.execute_script("location.reload()")


class Component:
    def __init__(self, driver):
        self.driver = driver
