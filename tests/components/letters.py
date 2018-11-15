# -*- coding: utf-8 -*-

from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

class Letters(Component):
    MAIL_FROM = '//span[@class="ll-crpt"]'
    MAIL_TEXT = '//span[@class="ll-sp__normal"]'
    MAIL_TIME = '//div[@class="llc__item llc__item_date"]'
    MAIL_IMAGE = '//div[@data-qa-id="avatar"]'
    SELECT_MESSAGE = '//a[contains(@class, "llc_normal")]'
    MOVE_TO_BUTTON = '//span[contains(text(), "Переместить в папку")]'
    NEW_FOLDER_FOR_LETTER = '//div[@title="{}"]'
    SELECT_ALL_MESSAGES_BUTTON = '//span[contains(text(), "Выделить все письма")]'

    @property
    def get_letters(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_elements_by_xpath(self.SELECT_MESSAGE)
        )

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

    def select_all_messages(self):
        letter = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SELECT_MESSAGE)
        )
        actionChains = ActionChains(self.driver)
        actionChains.context_click(letter).perform()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SELECT_ALL_MESSAGES_BUTTON)).click()

    def move_all_letters_to_folder(self, folder_name, topbar):
        self.select_all_messages()
        topbar.move_to_folder(folder_name)
        

    def move_letter_to_folder(self, folder_name):
        letter = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SELECT_MESSAGE)
        )
        actionChains = ActionChains(self.driver)
        actionChains.context_click(letter).perform()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MOVE_TO_BUTTON)).click()
        
        new_folder = self.NEW_FOLDER_FOR_LETTER.format(folder_name)
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(new_folder)).click()    