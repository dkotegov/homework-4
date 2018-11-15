# -*- coding: utf-8 -*-

from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

""" 
    Бар над списком писем.
    Дополнительные кнопки появляются при выделении нескольких писем.
"""
class Topbar(Component):
    BASE = '//div[@class="portal-menu js-shortcut"] '
    TOPBAR_BUTTONS = BASE + '//span[contains(text(), "{}")]'
    FOLDER_ELEM = './/a[@title="{}"]'

    def move_to_folder(self, folder_name):
        to_folder_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOPBAR_BUTTONS.format('В папку'))
        )
        to_folder_button.click()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FOLDER_ELEM.format(folder_name))
        ).click()



