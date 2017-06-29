# coding=utf-8
from selenium.webdriver.common.by import By

from base import *


class ListRepoPage(BaseElement):

    def repo_find(self, reponame):
        self.locator = (By.XPATH, "//a[contains(text(),'" + reponame + "')]")
        return self
