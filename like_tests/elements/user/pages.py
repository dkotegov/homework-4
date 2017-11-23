# -*- coding: utf-8 -*-

import os
from like_tests.elements.user.components import *
from like_tests.elements.page import Page


class AuthPage(Page):
    PATH = ''
    USER_LOGIN1 = 'technopark18'
    USER_LOGIN2 = 'technopark22'

    def login(self, login):
        password = os.environ['OK_PASSWORD']

        auth_form = self.form
        auth_form.set_login(login)
        auth_form.set_password(password)
        auth_form.submit()

    def login_user_1(self):
        self.login(self.USER_LOGIN1)

    def login_user_2(self):
        self.login(self.USER_LOGIN2)

    @property
    def form(self):
        return AuthForm(self.driver)


class UserPage(Page):
    PATH = ''

    def login_1(self):
        self.auth_page.login_user_1()
        return self.user_header.get_username()

    def login_2(self):
        self.auth_page.login_user_2()
        return self.user_header.get_username()

    def logout(self):
        LogoutButton(self.driver).click()
        LogoutConfirmButton(self.driver).click()

    @property
    def user_header(self):
        return UserHeader(self.driver)

    @property
    def auth_page(self):
        return AuthPage(self.driver)


