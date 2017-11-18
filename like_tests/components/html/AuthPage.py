# -*- coding: utf-8 -*-

import os

from like_tests.components.Page import Page
from like_tests.components.html.AuthForm import AuthForm


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
