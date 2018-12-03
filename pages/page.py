# coding=utf-8
import urlparse


class Page(object):
    BASE_URL = 'https://octavius.mail.ru/'
    PAGE = ''
    REDIRECT_QA = 'bundles/page.qa.html'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PAGE)
        self.driver.get(url)
        self.driver.fullscreen_window()

    def open_page_by_url(self, path):
        url = urlparse.urljoin(self.BASE_URL, path)
        self.driver.get(url)

    def redirectQA(self):
        url = urlparse.urljoin(self.BASE_URL, self.REDIRECT_QA)
        self.driver.get(url)

    def set_page(self, path):
        self.PAGE = path
