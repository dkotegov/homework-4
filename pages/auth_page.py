from pages.base_page import Page
from pages.login_form import LoginForm
from pages.navbar import NavBar


class AuthPage(Page):
    PATH = ''

    @property
    def navbar(self):
        return NavBar(self.driver)

    @property
    def login_form(self):
        return LoginForm(self.driver)

