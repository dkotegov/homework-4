from urllib.parse import urljoin

from pages.base_page import Page


class BaseSteps(object):

    def __init__(self, driver, page=Page):
        self.page = page(driver)

    def open(self):
        url = urljoin(self.page.BASE_URL, self.page.PATH)
        self.page.driver.get(url)
        self.page.driver.maximize_window()
