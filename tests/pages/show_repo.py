# coding=utf-8
from base import BasePage
from tests.elements.show_repo import ShowRepo


class ShowRepoPage(BasePage):
    def __init__(self, driver, reponame):
        self.url = 'https://github.com/testfortp/' + str(reponame)
        super(ShowRepoPage, self).__init__(driver)

    def get_repo_gitignore(self):
        return ShowRepo(self.driver).gitignore().wait_for_visible().get().text
