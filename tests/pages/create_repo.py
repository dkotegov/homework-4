# coding=utf-8
import re

from base import BasePage
from tests.elements.create_repo import CreateRepoPage as CreateRepoPageElements

class CreateRepoPage(BasePage):
    url = 'https://github.com/new'

    def __init__(self, driver):
        self.driver = driver
        self.create_repo_elements = CreateRepoPageElements(driver)
        super(BasePage, self).__init__()

    def set_repo_name(self, reponame):
        repo_input = self.create_repo_elements.repo_input().wait_for_clickable().get()
        repo_input.click()
        repo_input.clear()
        repo_input.send_keys(reponame)
        return self

    def add_gitignore(self):
        gitignore = self.create_repo_elements.gitignore_button().wait_for_clickable().get()
        gitignore.click()

        select_gitignore = self.create_repo_elements.gitignore_select().wait_for_clickable().get()
        select_gitignore.click()
        return self

    def create(self, reponame):
        self.create_repo_elements.create_button().wait_for_clickable().get().click()
