# -*- coding: utf-8 -*-

from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class MailFile(Component):
    BASE = '//div[contains(concat(" ", normalize-space(@class), " "), ' + \
        '" layer-explorer-from-filesearch ")]'

    DIRECTORY = BASE + \
        '//*[contains(concat(" ", normalize-space(@class), " "), ' + \
        '" b-tree__item ")]//*[contains(text(), "{}")]'
    FILE = BASE + '//*[contains(concat(" ", normalize-space(@class), " "),' + \
        ' " b-filename__name ")]' \
                  '[contains(text(), "{}")]'
    BUTTON_ATTACH = BASE + '//*[@title="Прикрепить"]'

    def change_folder(self, folder):
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.DIRECTORY.format(folder)))
        ).click()

    def attach_mail_file(self, filename):
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable((By.XPATH, self.FILE.format(filename)))
        ).click()

        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable((By.XPATH, self.BUTTON_ATTACH))
        ).click()
