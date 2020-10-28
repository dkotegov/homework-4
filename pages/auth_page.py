# -*- coding: utf-8 -*-

from pages.base import Page
from components.auth_form import AuthForm


class AuthPage(Page):
    BASE_URL = 'http://account.mail.ru/'
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)
