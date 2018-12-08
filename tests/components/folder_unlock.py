# -*- coding: utf-8 -*-

from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from sidebar import Sidebar


class FolderUnlock(Component):
    BASE = '//div[@data-qa-id="layer-secure-folder"] '

    INPUT_PASSWORD = BASE + '//input[@data-qa-id="input"]'
    SUBMIT = BASE + '//span[@data-qa-id="submit"]'

    def is_created(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BASE)
        )
        element = self.driver.find_elements_by_xpath(self.BASE)
        return len(element) != 0

    def set_password(self, password):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INPUT_PASSWORD)
        ).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def unlock_folder(self, folder_name, password):
        sidebar = Sidebar(self.driver)
        sidebar.click_unlock_folder_by_name(folder_name)
        self.set_password(password)
        self.submit()
