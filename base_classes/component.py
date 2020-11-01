from selenium.webdriver.remote.webdriver import WebDriver


class Component(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver
