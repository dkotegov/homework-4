from page import Page
from tests.components.auth_form import AuthForm


class AuthPage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self.open()

    @property
    def form(self):
        return AuthForm(self.driver)
