# coding=utf-8
from StdSuites import null

import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import Component
from components.base_form import BaseForm


class FileAttachingForm(BaseForm):
    # file attach elements
    FILE_ATTACH_INPUT = '//button[@class="container--1mFoS type_wide--2rZSG color_base--3bx-5 hoverable--ys0Ko"]/input'
    file_attach_input_element = null

    # / html / body / div[10] / div[3] / div / div[1] / div[2] / div[3] / div[3]/div/div/div/button[1]/input

    def send_keys_to_input(self, data):
        self.file_attach_input_element.send_keys(data)


        # TODO дождаться загрузки файла!

        # WebDriverWait(self.driver, 30) \
        #     .until(lambda _ :

    def set_file_attach_input(self):
        self.file_attach_input_element = self.driver.find_element_by_xpath(self.FILE_ATTACH_INPUT)
