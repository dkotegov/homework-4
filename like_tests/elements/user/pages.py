# -*- coding: utf-8 -*-

import os
from like_tests.elements.user.components import UserHeader, AuthForm, LogoutButton, LogoutConfirmButton
from like_tests.elements.page import Page


class AuthPage(Page):
    PATH = ''
    USER_LOGIN = 'technopark18'

    def login(self):
        password = os.environ['OK_PASSWORD']

        auth_form = self.form
        auth_form.set_login(self.USER_LOGIN)
        auth_form.set_password(password)
        auth_form.submit()

    @property
    def form(self):
        return AuthForm(self.driver)


class UserPage(Page):
    PATH = ''

    def login(self):
        self.auth_page.open()
        self.auth_page.login()
        return self.user_header.get_username()

    def logout(self):
        LogoutButton(self.driver).click()
        LogoutConfirmButton(self.driver).confirm()

    @property
    def user_header(self):
        return UserHeader(self.driver)

    @property
    def auth_page(self):
        return AuthPage(self.driver)


