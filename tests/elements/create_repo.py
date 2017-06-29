# coding=utf-8
from selenium.webdriver.common.by import By

from base import *


class CreateRepoPage(BaseElement):

    def repo_input(self):
        self.locator = (By.XPATH, "//input[@id='repository_name']")
        return self

    def repo_created_notice(self):
        self.locator = (By.XPATH, "//h1[@class='public')]/strong[@itemprop='name']")
        return self

    def create_button(self):
        self.locator = (By.XPATH, "//button[contains(text(),'Create repository')]")
        return self

    def gitignore_button(self):
        self.locator = (By.XPATH, "//i[contains(text(),'Add .gitignore:')]")
        return self

    def gitignore_select(self):
        self.locator = (By.XPATH, "//div[contains(text(),'Android')]")
        return self
