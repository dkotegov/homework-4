# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Component(object):
    TIMEOUT = 30
    FREQUENCY = 0.1

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

    def click_element(self, xpath):
        self.find_element(xpath).click()

    def input_text_to_element(self, xpath, text):
        input_element = self.find_element(xpath)
        input_element.clear()
        input_element.send_keys(text)

    def upload_image(self, xpath, file_name):
        image_path = '../images/' + file_name
        self.find_element(xpath).send_keys(image_path)

    def get_element_text(self, xpath):
        return self.find_element(xpath).text

    def waiting_until_invisible(self, element):
        wait = WebDriverWait(self.driver, self.TIMEOUT, self.FREQUENCY)
        wait.until(ec.invisibility_of_element_located((By.XPATH, element)))
