import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import constants
from components.base_component import BaseComponent
from components.user_component import UserForm
from components.page import Page
from constants import profiles


class UserPage(Page):

    def __init__(self, driver, url):
        super(UserPage, self).__init__(driver)
        self.user_component = UserForm(self.driver)
        self.PAGE = url

    def add_to_friend(self):
        try:
            button = self.user_component.sent_request_add_to_friends().click()
        except NoSuchElementException:
            pass

    def accept_friend(self):
        try:
            button = self.user_component.accept_friend_request().click()
        except NoSuchElementException:
            if self.user_component.is_friend() == True:
                pass
            else:
                raise



