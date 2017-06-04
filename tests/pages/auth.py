# coding=utf-8
from main import *
from tests.elements.auth import *


class AuthPage(BasePage):
    url = 'http://ftest.tech-mail.ru/pages/index/'

    def sign_in(self, login, password):
        self.driver.get(self.url)

        # Ждём, пока document.readyState не станет равен 'complete'
        # Это означает, что всё загрузилось и все скрипты выполнены
        self.wait()

        OpenLoginFormButton(self.driver).wait_for_visible().get().click()

        LoginForm(self.driver).wait_for_visible()

        login_field = LoginInput(self.driver).super_wait(PasswordInput(self.driver)).get()
        login_field.click()
        login_field.clear()
        login_field.send_keys(login)

        password_field = PasswordInput(self.driver).wait_for_visible().get()
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        SubmitLoginButton(self.driver).wait_for_visible().get().click()

        MainPage(self.driver).wait_username()
