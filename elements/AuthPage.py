# -*- coding: utf-8 -*-

from elements.Page import Page
from elements.AuthForm import AuthForm
from elements.TopMenu import TopMenu

class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def top_menu(self):
        return TopMenu(self.driver)