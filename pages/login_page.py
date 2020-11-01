from base_classes.page import Page
from components.login_form import LoginForm


class LoginPage(Page):
    PATH = 'login'

    @property
    def login_form(self):
        return LoginForm(self.driver)
