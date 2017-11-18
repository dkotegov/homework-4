# -*- coding: utf-8 -*-

from like_tests.components.Page import Page
from like_tests.components.html.AuthPage import AuthPage
from like_tests.components.html.UserHeader import UserHeader


class UserPage(Page):
    PATH = ''

    def login(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login()

        return self.user_header.get_username()

    @property
    def user_header(self):
        return UserHeader(self.driver)
