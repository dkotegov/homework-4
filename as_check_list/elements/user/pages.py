# -*- coding: utf-8 -*-

import os
from as_check_list.elements.user.components import *
from as_check_list.elements.page import Page


class UserPage(Page):
    USER_LOGIN1 = 'technopark18'
    USER_NAME1 = u'Имярек Человекович'
    USER_PATH1 = 'imyarek.chelovekovich'
    USER_LOGIN2 = 'technopark22'
    USER_NAME2 = u'Кадыр Рамзанов'
    USER_PATH2 = '/profile/571379518273'

    @staticmethod
    def check_page(driver, user_path):
        user_page = UserPage(driver, user_path)
        user_page.open()

    def login(self, login):
        password = os.environ['PASSWORD']
        self.auth_form.set_login(login)
        self.auth_form.set_password(password)
        self.auth_form.submit()

    def login_1(self):
        self.login(self.USER_LOGIN1)
        return self.user_header.get_username()

    def login_2(self):
        self.login(self.USER_LOGIN2)
        return self.user_header.get_username()

    def open_own_feed(self):
        self.user_header.click()

    def logout(self):
        self.logout_button.click()
        self.logout_confirm_button.click()

    def is_logged_out(self):
        return self.auth_form.is_logged_out()

    @property
    def user_header(self):
        return UserHeader(self.driver)

    @property
    def logout_button(self):
        return LogoutButton(self.driver)

    @property
    def logout_confirm_button(self):
        return LogoutConfirmButton(self.driver)

    @property
    def auth_form(self):
        return AuthForm(self.driver)
