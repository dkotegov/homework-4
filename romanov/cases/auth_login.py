import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from romanov.steps.auth import Steps

from romanov.app.driver import connect


class AuthLoginTest(unittest.TestCase):
    def test_auth_login_success(self):
        auth = Steps()
        auth.open_app()
        auth.open_login()
        auth.enter_login_data()
        auth.login()

    def test_auth_login_user_non_exist(self):
        auth = Steps()
        auth.open_app()
        auth.open_login()
        auth.enter_login("test32373827")
        auth.enter_pass("test32373827")
        auth.click_login()
        auth.find_info_error()

    def test_auth_login_empty_data(self):
        auth = Steps()
        auth.open_app()
        auth.open_login()
        auth.enter_login("")
        auth.enter_pass("")
        auth.click_login()
        auth.find_info_error()

    def test_auth_login_refresh_page(self):
        auth = Steps()
        auth.open_app()
        auth.open_login()
        auth.enter_login_data()
        auth.login()
        auth.open_app()
        auth.find_auth_menu()
