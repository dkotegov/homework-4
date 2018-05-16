# -*- coding: utf-8 -*-
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Component(object):
    TIMEOUT = 30
    FREQUENCY = 0.1

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element):
        return WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY).until(
            lambda d: d.find_element_by_xpath(element)
        )

    def click_element(self, element):
        WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY).until(
            lambda d: d.find_element_by_xpath(element)
        ).click()

    def input_text_to_element(self, element, text):
        input_element = WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY).until(
            lambda d: d.find_element_by_xpath(element)
        )
        input_element.clear()
        input_element.send_keys(text)

    def upload_image(self, element, file_name):
        image_path = os.getcwd() + '/images/' + file_name
        WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY).until(
            lambda d: d.find_element_by_xpath(element)
        ).send_keys(image_path)

    def get_element_text(self, element):
        return WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY).until(
            lambda d: d.find_element_by_xpath(element).text
        )

    def waiting_until_invisible(self, element):
        wait = WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY)
        wait.until(ec.invisibility_of_element_located((By.XPATH, element)))
