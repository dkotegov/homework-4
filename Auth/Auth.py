# -*- coding: utf-8 -*-

from Base import Component
from Base import Page


class AuthForm(Component):
    LOGIN = '//input[@name="username"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//button[@data-test-id="submit-button"]'
    NEXT_BUTTON = '//button[@data-test-id="next-button"]'
    LOGIN_BUTTON = '//a[text()="Войти"]'

    def set_login(self, login):
        self._wait_until_and_click_elem_by_xpath(self.LOGIN).send_keys(login)

    def click_next(self):
        self._wait_until_and_click_elem_by_xpath(self.NEXT_BUTTON).click()

    def set_password(self, pwd):
        self._wait_until_and_click_elem_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self._wait_until_and_click_elem_by_xpath(self.SUBMIT).click()

    def wait_for_cookie(self):
        self._wait_for_url('https://e.mail.ru/inbox/?afterReload=1')


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    def auth(self, login, password):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.form.set_login(login)
        auth_page.form.click_next()
        auth_page.form.set_password(password)
        auth_page.form.submit()
        auth_page.form.wait_for_cookie()
