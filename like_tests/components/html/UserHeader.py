# -*- coding: utf-8 -*-

from like_tests.components.Component import Component
from selenium.webdriver.support.wait import WebDriverWait


class UserHeader(Component):
    USERNAME = '//h1[@class="mctc_name_tx bl"]'
    TIMEOUT = 5
    POLL_FREQUENCY = 0.1

    def get_username(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.POLL_FREQUENCY).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )
