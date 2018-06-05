# -*- coding: utf-8 -*-
import os
import re

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Component(object):
    TIMEOUT = 30
    FREQUENCY = 0.1

    NUMBER_OF_FIRST_CHARS = 83

    @staticmethod
    def get_number_from_string(string):
        return int(re.search(r'\d+', string).group())

    @staticmethod
    def get_first_part_of_image_src(src):
        return src[:Component.NUMBER_OF_FIRST_CHARS]

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, xpath):
        return WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY).until(
            lambda d: d.find_element_by_xpath(xpath)
        )

    def is_exist_element(self, xpath):
        try:
            self.find_element(xpath)
        except TimeoutException:
            return False
        return True

    def is_not_exist_element(self, xpath):
        try:
            self.waiting_until_invisible(xpath)
        except TimeoutException:
            return False
        return True

    def click_element(self, xpath):
        self.find_element(xpath).click()

    def input_text_to_element(self, xpath, text):
        input_element = self.find_element(xpath)
        input_element.clear()
        input_element.send_keys(text)

    def upload_image(self, xpath, file_name):
        image_folder = os.environ.get('IMAGES', 'images/')
        image_path = image_folder + file_name
        self.find_element(xpath).send_keys(image_path)

    def get_element_text(self, xpath):
        return self.find_element(xpath).text

    def waiting_until_invisible(self, element):
        wait = WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY)
        wait.until(ec.invisibility_of_element_located((By.XPATH, element)))

    def waiting_until_visible(self, element):
        wait = WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY)
        wait.until(ec.visibility_of_element_located((By.XPATH, element)))
