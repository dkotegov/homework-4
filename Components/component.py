# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait


class Component(object):
    TIMEOUT = 30
    FREQUENCY = 0.1

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, element):
        WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY).until(
            lambda d: d.find_element_by_xpath(element)
        ).click()

    def input_text_to_element(self, element, text):
        WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY).until(
            lambda d: d.find_element_by_xpath(element)
        ).send_keys(text)

    def get_element_text(self, element):
        return WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY).until(
            lambda d: d.find_element_by_xpath(element).text
        )
