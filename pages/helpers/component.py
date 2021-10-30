from helpers import Helpers


class Component(object):
    def __init__(self, driver):
        self.driver = driver
        self.helpers = Helpers(driver=driver)
