# -*- coding: utf-8 -*-

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os


class Component(object):
    def __init__(self, driver):
        self.driver = driver
        self.TEST_USER_PASSWORD = os.environ.get('HW4PASSWORD', 'passw0rd')

    def click(self, item):
        element = self.driver.find_element_by_xpath(item)
        return element.click()

    def send_keys(self, item, keys):
        element = WebDriverWait(self.driver, 40).until(ec.element_to_be_clickable((By.XPATH, item)))
        return element.send_keys(keys)

    def hover(self, item):
        link = self.driver.find_element_by_xpath(item)
        hover = ActionChains(self.driver).move_to_element(link)
        hover.perform()
