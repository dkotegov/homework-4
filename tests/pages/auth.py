# coding=utf-8

from main import *
from tests.elements.auth import *


class AuthPage(BasePage):
    url = 'http://ftest.tech-mail.ru/pages/index/'

    def sign_in(self, login, password):
        self.navigate()

        OpenLoginFormButton(self.driver).get().click()

        login_field = LoginInput(self.driver).get()
        login_field.value = ""
        login_field.click()
        login_field.send_keys(login)

        password_field = PasswordInput(self.driver).get()
        password_field.value = ""
        password_field.click()
        password_field.send_keys(password)

        SubmitLoginButton(self.driver).get().click()

        MainPage(self.driver).wait_username()
