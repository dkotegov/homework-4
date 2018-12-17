from page import Page
from tests.components.auth_form import AuthForm


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)
