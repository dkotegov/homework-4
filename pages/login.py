from pages.default import Page
from components.login_form import LoginForm

from utils import wait_for_url


class LoginPage(Page):
    PATH = "login/"

    def auth(self):
        self.open()
        form = LoginForm(self.driver)
        form.set_login('user@user.ru')
        form.set_password('password')
        form.submit()
        wait_for_url(self.driver, self.BASE_URL)
