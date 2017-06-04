# coding=utf-8


class BasePage(object):
    DEFAULT_WAIT_TIME = 10
    ELEMENT_NOT_PRESENT_TIME = 2
    url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)
