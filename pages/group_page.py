import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import constants
from components.base_component import BaseComponent
from components.group_form import GroupForm
from components.page import Page
from constants import profiles


class GroupPage(Page):

    def __init__(self, driver):
        super(GroupPage, self).__init__(driver)
        self.group_form = GroupForm(self.driver)
        self.PAGE = "/carsguru"

    def group_add(self):
        self.group_form.group_add().click()

    def group_delete(self):
        self.group_form.group_menu().click()
        self.group_form.group_delete().click()