# -*- coding: utf-8 -*-


class Component(object):
    TIMEOUT = 5
    POLL_FREQUENCY = 0.1

    def __init__(self, driver):
        # type: (object) -> object
        self.driver = driver


class Clickable(Component):
    CLICK = ''

    def click(self):
        self.driver.find_element_by_xpath(self.CLICK).click()

    def find(self):
        self.driver.find_element_by_xpath(self.CLICK)

    @staticmethod
    def hard_click(driver, xpath):
        driver.execute_script('arguments[0].click();', driver.find_element_by_xpath(xpath))
