from pages.BasePage import Page


class Steps(object):
    def __init__(self, driver):
        self.driver = driver
        self.page = Page(driver)

    def open_page(self):
        self.page.open()

    def get_page_title(self):
        return self.page.get_title()
