import urlparse


class Page(object):
    BASE_URL = u'https://e.mail.ru/'
    PATH = u''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()