# -*- coding: utf-8 -*-

from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Letters(Component):
    LETTER_AVATAR = '//a[@title="{}"]/*/button[@class="ll-av ll-av_size_common stop-animate"]'
    LETTER = '//a[@title="{}"] [@data-shortcut="list-letter"]'
    DIRECTORY = '//a[@title="{}"] [@class="nav__item nav__item_shortcut"]'

    def select_letter_by_subject(self, subject):
        select_letter = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LETTER_AVATAR.format(subject))
        )
        select_letter.click()

    def drag_and_drop_letter_to_dir(self, letter_subject, dir_name):

        letter = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LETTER)
        )

        directory = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DIRECTORY)
        )
        
        ActionChains(self.driver).drag_and_drop(letter, directory).perform()