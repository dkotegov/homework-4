import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

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
        except TimeoutException:
            pass

    def is_friend(self):
        return self.user_component.is_friend()


    def accept_friend(self):
        try:
            button = self.user_component.accept_friend_request().click()
        except TimeoutException:
            if self.user_component.is_friend() == True:
                pass
            else:
                raise

    def age(self):
        return self.user_component.age().text

    def del_friend(self):
        self.user_component.button_menu_friends().click()
        self.user_component.button_del_friend().click()


