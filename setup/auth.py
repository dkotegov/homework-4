# -*- coding: utf-8 -*-
from pages.auth_page import AuthPage
import time


def setup_auth(test):
    auth_page = AuthPage(test.driver)
    auth_page.open()
    auth_form = auth_page.form
    auth_form.set_login(test.EMAIL)
    auth_form.to_password()
    auth_form.set_password(test.PASSWORD)
    auth_form.submit()
    auth_form.wait_for_email()
