from components.auth_form import AuthForm
from pages.page import Page


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)
