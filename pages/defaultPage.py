
class Page(object):
    BASE_URL = 'https://zinterest.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = self.BASE_URL + self.PATH
        # urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()



class Component(object):
    BASE_URL = 'https://zinterest.ru/'
    def __init__(self, driver):
        self.driver = driver
