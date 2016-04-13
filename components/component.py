# -*- coding: utf-8 -*-

from selenium.webdriver import ActionChains


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def click(self, item):
        return self.driver.find_element_by_xpath(item).click()

    def hover(self, item):
        link = self.driver.find_element_by_xpath(item)
        hover = ActionChains(self.driver).move_to_element(link)
        hover.perform()

