# -*- coding: utf-8 -*-

from component import Component
from folder_create import FolderCreate
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

"""
    Бар над списком писем.
    Дополнительные кнопки появляются при выделении нескольких писем.
"""


class Topbar(Component):
    BASE = '//div[@class="portal-menu js-shortcut"] '
    TOPBAR_BUTTONS = BASE + '//span[contains(text(), "{}")]'

    TO_FOLDER_CONTEXT_MENU = BASE + '//div[@data-qa-id="folders"]'
    FOLDER_ELEM = TO_FOLDER_CONTEXT_MENU + '//a[@title="{}"]'
    NEW_DIR_ELEM = TO_FOLDER_CONTEXT_MENU + \
        '//div[@data-qa-id="new-folder-btn"]'

    DELETE = BASE + '//*[@data-qa-id="delete"]'
    SELECT_ALL_MESSAGES_BUTTON = '//*[@data-qa-id="select-all"]'

    def move_to_folder(self, folder_name):
        top_bar_button = 'В папку'

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.TOPBAR_BUTTONS.format(top_bar_button))
        ).click()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.FOLDER_ELEM.format(folder_name))
        ).click()

    def move_to_new_folder(self, folder_name):
        top_bar_button = 'В папку'
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.TOPBAR_BUTTONS.format(top_bar_button))
        ).click()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NEW_DIR_ELEM)
        ).click()

        folder_create = FolderCreate(self.driver)

        folder_create.set_name(folder_name)
        folder_create.submit()

    def move_to_archive(self):
        top_bar_button = 'В архив'
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.TOPBAR_BUTTONS.format(top_bar_button))
        ).click()

    def delete(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE)
        ).click()

    def select_all(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.SELECT_ALL_MESSAGES_BUTTON))
        ).click()
