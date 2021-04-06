from pages.base_page import Page


class Steps(object):
    def __init__(self, driver):
        self.driver = driver
        self.page = Page(driver)

    def open_page(self, path=None):
        self.page.open(path)

    def get_page_title(self):
        return self.page.get_title()

    def get_page_url(self):
        return self.page.get_url()
