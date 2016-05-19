# -*- coding: utf-8 -*-

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def click(self, item):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        return element.click()

    def send_keys(self, item, keys):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
        return element.send_keys(keys)
        # return self.driver.find_element_by_xpath(item).click()

    def hover(self, item):
        link = self.driver.find_element_by_xpath(item)
        hover = ActionChains(self.driver).move_to_element(link)
        hover.perform()
