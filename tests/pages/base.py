# coding=utf-8
import time

from tests.elements.main import UserDropdown


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)
        UserDropdown(self.driver).check_user_nav().wait_for_presence()
