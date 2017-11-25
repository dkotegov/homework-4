# -*- coding: utf-8 -*-

import os
from like_tests.elements.user.components import *
from like_tests.elements.page import Page


class AuthPage(Page):
    PATH = ''
    USER_LOGIN1 = 'technopark18'
    USER_NAME1 = u'Имярек Человекович'
    USER_LOGIN2 = 'technopark22'
    USER_NAME2 = u'Кадыр Рамзанов'

    def login(self, login):
        password = os.environ['OK_PASSWORD']
        self.form.set_login(login)
        self.form.set_password(password)
        self.form.submit()

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
        self.logout_button.click()
        self.logout_confirm_button.click()

    def is_logged_out(self):
        return self.auth_page.form.is_logged_out()

    @property
    def user_header(self):
        return UserHeader(self.driver)

    @property
    def auth_page(self):
        return AuthPage(self.driver)

    @property
    def logout_button(self):
        return LogoutButton(self.driver)

    @property
    def logout_confirm_button(self):
        return LogoutConfirmButton(self.driver)
