from urllib.parse import urljoin


class Page(object):
    SECUREBUTTON = '//button[@id="details-button"]'
    GO = '//a[@id="proceed-link"]'
    BASE_URL = 'https://kino-park.online'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.find_element_by_xpath(self.SECUREBUTTON).click()
        self.driver.find_element_by_xpath(self.GO).click()
        self.driver.maximize_window()
