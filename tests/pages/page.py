# coding=utf-8
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    BASE_URL = 'http://localhost:5007/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = self.BASE_URL + self.PATH
        self.driver.get(url)
        # self.driver.maximize_window()

    def reload(self):
        self.driver.refresh()

    def alert_accept(self):
        try:
            WebDriverWait(self.driver, 10, 0.1).until(
                EC.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            alert_text = "no alert"
        return alert_text

    def alert_input_and_accept(self, input_int):
        try:
            WebDriverWait(self.driver, 10, 0.1).until(
                EC.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            alert.send_keys(str(input_int))
            alert.accept()
        except TimeoutException:
            print "no alert"
