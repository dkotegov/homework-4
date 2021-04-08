import components
from pages.base_page import BasePage
from components.auth_form import AuthForm


class AuthPage(BasePage):
    BASE_URL = 'https://studhunt.ru/'
    PATH = 'auth'

    @property
    def form(self) -> components.auth_form:
        return AuthForm(self.driver)
