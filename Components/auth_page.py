# -*- coding: utf-8 -*-
from Components.component import Component


class AuthForm(Component):
    LOGIN = '//input[@id="field_email"]'
    PASSWORD = '//input[@id="field_password"]'
    SUBMIT = '//input[contains(@data-l,"sign_in")]'

    def set_login(self, login):
        super(AuthForm, self).input_text(self.LOGIN, login)

    def set_password(self, password):
        super(AuthForm, self).input_text(self.PASSWORD, password)

    def submit(self):
        super(AuthForm, self).click_element(self.SUBMIT)
