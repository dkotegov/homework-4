# coding=utf-8
import re

from base import BasePage
from tests.elements.list_repos import ListRepoPage as ListRepoPageElements


class ListRepoPage(BasePage):
    url = 'https://github.com/testfortp?tab=repositories'

    def __init__(self, driver):
        self.driver = driver
        self.list_repo_elements = ListRepoPageElements(driver)
        super(BasePage, self).__init__()

    def check_repo_exist(self, reponame):
        return self.list_repo_elements.repo_find(reponame).is_existed() is False
