from urllib.parse import urljoin


class BaseSteps(object):

    def __init__(self, driver, page):
        self.page = page(driver)

    def open(self):
        url = urljoin(self.page.BASE_URL, self.page.PATH)
        self.page.driver.get(url)
        self.page.driver.maximize_window()
