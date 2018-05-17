import sys
from selenium import webdriver

import constants
from components.auth_form import AuthForm
from components.base_component import BaseComponent
from components.page import Page
from constants import profiles


class AuthPage(Page):
    LOGOUT_URL = 'https://ok.ru/dk?st.cmd=anonymMain&st.layer.cmd=PopLayerClose'

    def __init__(self, driver):
        super(AuthPage, self).__init__(driver)
        self.auth_form = AuthForm(self.driver)

    def login(self, login, password):
        self.auth_form.get_login().send_keys(login)
        self.auth_form.get_password().send_keys(password)
        self.auth_form.submit().click()

    def logout(self):
        self.driver.get(self.LOGOUT_URL)
        # self.auth_form.get_logout_bar().click()
        # self.auth_form.get_logout_button().click()
        # self.auth_form.get_confirm_logout_button().click()

    def add_profile(self, login, password):
        self.auth_form.get_add_profile_button().click()
        self.login(login, password)

    #def already_login(self):





