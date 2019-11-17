# coding=utf-8
from pages.common import Page, Component


class AuthPage(Page):
    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(Component):
    LOGIN = '//input[@name="Login"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = '//button[@data-test-id="submit-button"]'
    SUBMIT_ACCOUNT_NAME = '//button[@data-test-id="next-button"]'

    def set_login(self, login):
        login_input = self.wait_for_visible(self.LOGIN)
        login_input.send_keys(login)

    def set_password(self, pwd):
        password_input = self.wait_for_visible(self.PASSWORD)
        password_input.send_keys(pwd)

    def submit_account_name(self):
        submit = self.wait_for_visible(self.SUBMIT_ACCOUNT_NAME)
        submit.click()

    def submit(self):
        submit = self.wait_for_visible(self.SUBMIT)
        submit.click()
