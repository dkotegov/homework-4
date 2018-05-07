# -*- coding: utf-8 -*-
from Components.component import Component


class AuthForm(Component):
    LOGIN = '//input[@id="field_email"]'
    PASSWORD = '//input[@id="field_password"]'
    SUBMIT = '//input[@class="button-pro __wide"]'

    def set_login(self, login):
        super(AuthForm, self).input_text_to_element(self.LOGIN, login)

    def set_password(self, password):
        super(AuthForm, self).input_text_to_element(self.PASSWORD, password)

    def submit(self):
        super(AuthForm, self).click_element(self.SUBMIT)
