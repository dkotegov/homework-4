import urlparse


class Page(object):
    BASE_URL = 'https://octavius.mail.ru/'
    PAGE = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PAGE)
        self.driver.get(url)
        # self.driver.fullscreen_window()
        self.driver.maximize_window()

    def open_page_by_url(self, path):
        url = urlparse.urljoin(self.BASE_URL, path)
        self.driver.get(url)
        # self.driver.maximize_window()

    def set_page(self, path):
        self.PAGE = path
