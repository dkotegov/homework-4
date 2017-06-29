# coding=utf-8
from base import BasePage
from tests.elements.auth import LoginForm
from tests.pages.main import MainPage


class AuthPage(BasePage):
    url = 'https://github.com/login'

    def sign_in(self, login, password):
        self.driver.get(self.url)

        login_form = LoginForm(self.driver)

        login_field = login_form.login_input().wait_for_clickable().get()
        login_field.click()
        login_field.clear()
        login_field.send_keys(login)

        password_field = login_form.password_input().wait_for_visible().get()
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_form.sign_in_button().wait_for_visible().get().click()

        MainPage(self.driver).wait_username()
