import sys
from selenium import webdriver

from components.auth_form import AuthForm
from components.base_component import BaseComponent
from components.page import Page


class AuthPage(Page):

    def login(self, login, password):
        auth_form = AuthForm(self.driver)
        auth_form.get_login().send_keys(login)
        auth_form.get_password().send_keys(password)
        auth_form.submit().click()



