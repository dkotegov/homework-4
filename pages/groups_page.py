import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import constants
from components.base_component import BaseComponent
from components.groups_form import GroupsForm
from components.page import Page
from constants import profiles


class GroupsPage(Page):

    def __init__(self, driver, url):
        super(GamesPage, self).__init__(driver)
        self.groups_form = GroupsForm(self.driver)
        self.PAGE = url + "/groups"

    def groups_visibility(self):
        try:
            self.groups_form.groups_container()
            return True
        except TimeoutException:
            return False
