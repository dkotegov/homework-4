
# coding=utf-8
from selenium.webdriver.common.by import By

from base import BaseElement


class RemoveButtons(BaseElement):

    def submit_remove_button(self):
        self.locator = (By.XPATH, "(//button[text()[contains(.,'I understand')]])[4]")
        return self

    def remove_button(self):
        self.locator = (By.XPATH, "//button[contains(text(),'Delete this repository')]")
        return self


    def reponame_input(self):
        self.locator = (By.XPATH, "(//input[@aria-label[contains(.,'Type in the name of the repository to confirm that you want to delete this repository.')]])[2]")
        return self

    def delete_form(self):
        self.locator = (By.XPATH, "//div[@class='facebox-popup']")
        return self

    def reponame_new_input(self):
        self.locator = (By.XPATH, "//input[@name='new_name']")
        return self

    def submit_rename_repo(self):
        self.locator = (By.XPATH, "//button[contains(@class, 'js-rename-repository-button')]")
        return self
