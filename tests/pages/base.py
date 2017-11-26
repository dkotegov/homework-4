# coding=utf-8
import time

from tests.elements.main import MainElements


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)
        MainElements(self.driver).user_email().wait_for_presence()
