# -*- coding: utf-8 -*-

from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

class Letters(Component):
    MAIL_FROM = '//span[@class="ll-crpt"]'
    MAIL_TEXT = '//span[@class="ll-sp__normal"]'
    MAIL_TIME = '//div[@class="llc__item llc__item_date"]'
    SELECT_MESSAGE = '//a[contains(@class, "llc_normal")]'
    MOVE_TO_BUTTON = '//span[contains(text(), "Переместить в папку")]'
    NEW_FOLDER_FOR_LETTER = '//div[@title="{}"]'

    def get_mail_from(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIL_FROM).text
        )

    def get_mail_text(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIL_TEXT).text
        )

    def get_mail_time(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIL_TIME).text
        )

    def move_letters_to_folder(self, folder_name):
        folder = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SELECT_MESSAGE)
        )
        actionChains = ActionChains(self.driver)
        actionChains.context_click(folder).perform()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MOVE_TO_BUTTON)).click()
        
        new_folder = self.NEW_FOLDER_FOR_LETTER.format(folder_name)
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(new_folder)).click()