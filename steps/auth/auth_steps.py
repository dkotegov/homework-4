import os

from steps.base_steps import BaseSteps
from pages.auth_page import AuthPage


class AuthSteps(BaseSteps):
    EMAIL = os.environ['EMAIL']
    PASSWORD = os.environ['PASSWORD']

    def __init__(self, driver, page=None):
        super().__init__(driver, AuthPage)

    def auth(self):
        self.open()
        self.page.container.wait_for_container()
        self.login()
        self.page.wait_for_url('https://e.mail.ru/inbox/?afterReload=1')

    def login(self):
        login_form = self.page.login_form
        login_form.set_login(self.EMAIL)
        login_form.next()
        login_form.set_password(self.PASSWORD)
        login_form.submit()
