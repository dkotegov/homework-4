# -*- coding: utf-8 -*-

import os
from like_tests.elements.user.components import UserHeader, AuthForm
from like_tests.elements.page import Page


class AuthPage(Page):
    PATH = ''
    USER_LOGIN = 'technopark18'

    @property
    def form(self):
        return AuthForm(self.driver)

    def login(self):
        password = os.environ['OK_PASSWORD']

        auth_form = self.form
        auth_form.set_login(self.USER_LOGIN)
        auth_form.set_password(password)
        auth_form.submit()


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


