from components.auth.login_form_component import LoginForm
from pages.base_page import Page
from steps.base_steps import BaseSteps
from steps.mainpage.main_page_steps import MainSteps


class AuthPage(Page):
    BASE_URL = 'https://account.mail.ru/'
    PATH = ''
    ROOT = '[data-test-id=login-app-ready]'


    @property
    def login_form(self):
        return LoginForm(self)

    @property
    def base_steps(self):
        return BaseSteps(self.driver)
