# coding=utf-8
from base import BasePage
from tests.elements.remove_repo import RemoveButtons
import time


class RemoveRepoPage(BasePage):
    def __init__(self, driver, username, reponame):
        self.url = 'https://github.com/' + username + '/' + str(reponame) + '/settings'
        self.setting_repo_elements = RemoveButtons(driver)
        super(RemoveRepoPage, self).__init__(driver)

    def submit_remove(self, reponame):
        self.setting_repo_elements.remove_button().wait_for_clickable().get().click()
        self.setting_repo_elements.delete_form().wait_for_visible()

        reponame_input = self.setting_repo_elements.reponame_input().wait_for_clickable().get()
        reponame_input.click()
        reponame_input.clear()
        reponame_input.send_keys(reponame)

        self.setting_repo_elements.submit_remove_button().wait_for_clickable().get().click()

    def rename_repo(self, new_reponame):
        rename_input = self.setting_repo_elements.reponame_new_input().wait_for_clickable().get()
        rename_input.click()
        rename_input.clear()
        rename_input.send_keys(new_reponame)

    def submit_rename(self):
        self.setting_repo_elements.submit_rename_repo().wait_for_clickable().get().click()
