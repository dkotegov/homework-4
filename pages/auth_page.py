import os

from pages.default_page import DefaultPage, Component
from helpers import wait_for_element


class AuthPage(DefaultPage):
    URL = 'https://account.mail.ru'

    @property
    def form(self):
        return AuthForm(self.driver)


    def authorize(self, login=os.environ['LOGIN'], password=os.environ['PASSWORD']):
        auth_form = AuthForm(self.driver)

        auth_form.set_login(login)
        auth_form.next()
        auth_form.set_password(password)
        auth_form.submit()


class AuthForm(Component):
    LOGIN = 'input[name="Login"]'
    PASSWORD = 'input[name="Password"]'
    NEXT = '[data-test-id="next-button"]'
    SUBMIT = '[data-test-id="submit-button"]'

    def set_login(self, login):
        element = wait_for_element(self.driver, self.LOGIN)
        element.send_keys(login)

    def set_password(self, pwd):
        element = wait_for_element(self.driver, self.PASSWORD)
        element.send_keys(pwd)

    def next(self):
        element = wait_for_element(self.driver, self.NEXT)
        element.click()
        
    def submit(self):
        element = wait_for_element(self.driver, self.SUBMIT)
        element.click()
