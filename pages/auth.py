from pages.default import Page
from components.auth_form import AuthForm

from utils import wait_for_url


class AuthPage(Page):
    PATH = "login/"

    def auth(self):
        self.open()
        form = AuthForm(self.driver)
        form.set_login('user@user.ru')
        form.set_password('password')
        form.submit()
        wait_for_url(self.driver, self.BASE_URL)
