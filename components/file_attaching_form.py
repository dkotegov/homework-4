# coding=utf-8
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

    # / html / body / div[10] / div[3] / div / div[1] / div[2] / div[3] / div[3]/div/div/div/button[1]/input

    def get_file_attach_input(self):
        return self.driver.find_element_by_xpath(self.FILE_ATTACH_INPUT)


