import os
from time import sleep

from steps.base_steps import BaseSteps
from pages.auth_page import AuthPage


class AuthSteps(BaseSteps):
    EMAIL = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def __init__(self, driver, page=None):
        super().__init__(driver, AuthPage)

    def auth(self):
        self.open()
        self.page.container.wait_for_container()
        self.login()
        self.page.wait_for_url('https://e.mail.ru/inbox/?afterReload=1')

    def auth_main_page(self):
        self.auth()
        main_steps = self.page.base_steps
        main_steps.open()
        self.page.waiting_for_visible_by_selector(main_steps.page.ROOT)

    def login(self):
        login_form = self.page.login_form
        login_form.set_login(self.EMAIL)
        login_form.next()
        login_form.set_password(self.PASSWORD)
        login_form.submit()
