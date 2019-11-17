import os

from pages.default_page import DefaultPage, Component
from helpers import wait_for_element


class AuthPage(DefaultPage):
    URL = 'https://account.mail.ru'

    @property
    def form(self):
        return AuthForm(self.driver)


    def authorize(self, login='yekaterina.kirillova.1998@bk.ru', password='qwerYtuarRyYY12'):
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
        wait_for_element(self.driver, self.LOGIN)
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        wait_for_element(self.driver, self.PASSWORD)
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(pwd)

    def next(self):
        wait_for_element(self.driver, self.NEXT)
        self.driver.find_element_by_css_selector(self.NEXT).click()
        
    def submit(self):
        wait_for_element(self.driver, self.SUBMIT)
        self.driver.find_element_by_css_selector(self.SUBMIT).click()
