# -*- coding: utf-8 -*-
import os
import re

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Component(object):
    TIME_FOR_IMPLICIT_WAIT = 1
    VISIBILITY_TIMEOUT = 30
    IMAGE_UPLOAD_TIMEOUT = 90
    FREQUENCY = 0.1

    @staticmethod
    def get_number_from_string(string):
        return int(re.search(r'\d+', string).group())

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(self.TIME_FOR_IMPLICIT_WAIT)

    def find_element(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_elements(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def get_number_of_elements(self, xpath):
        return len(self.find_elements(xpath))

    def is_exist_element(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def click_element(self, xpath):
        self.find_element(xpath).click()

    def input_text(self, xpath, text):
        self.input_key(xpath, text)

    def input_key(self, xpath, key):
        self.find_element(xpath).send_keys(key)

    def get_element_text(self, xpath):
        return self.find_element(xpath).text

    def upload_image(self, xpath, file_name):
        image_folder = os.environ.get('IMAGES', 'images/')
        image_path = os.path.abspath(image_folder + file_name)
        self.find_element(xpath).send_keys(image_path)

    def get_image_source(self, xpath):
        image_element = WebDriverWait(self.driver, self.IMAGE_UPLOAD_TIMEOUT, self.FREQUENCY).until(
            lambda d: d.find_element_by_xpath(xpath)
        )
        full_image_src = image_element.get_attribute("src")
        NUMBER_OF_FIRST_CHARS = 80
        return full_image_src[:NUMBER_OF_FIRST_CHARS]

    def waiting_until_invisible(self, element):
        wait = WebDriverWait(self.driver, self.VISIBILITY_TIMEOUT, self.FREQUENCY)
        wait.until(ec.invisibility_of_element_located((By.XPATH, element)))

    def waiting_until_visible(self, element):
        wait = WebDriverWait(self.driver, self.VISIBILITY_TIMEOUT, self.FREQUENCY)
        wait.until(ec.visibility_of_element_located((By.XPATH, element)))
