import urllib.parse


class Page(object):
    BASE_URL = 'https://park.vk.company/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urllib.urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
