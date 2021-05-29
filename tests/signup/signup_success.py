import os

import unittest
from tests.default_setup import default_setup
from steps.delete_user import delete_user
from steps.get_profile_login import get_profile_login
from Pages.signup_page import SignupPage

class SignupSuccessTests(unittest.TestCase):
    signup_login_success = "abrikos-soska"
    signup_password = "12345678"
    signup_mail = "qwer@mail.ru"

    def setUp(self):
        default_setup(self)
        self.signup_page = SignupPage(self.driver)

    def tearDown(self):
        delete_user(self)
        self.driver.quit()

    def test_signup_success(self):
        self.signup_page.open()
        self.signup_page.set_login(self.signup_login_success)
        self.signup_page.set_password(self.signup_password)
        self.signup_page.set_mail(self.signup_mail)
        self.signup_page.submit()
        self.signup_page.wait_for_account()
        login_in_profile = get_profile_login(self)
        self.assertEqual(login_in_profile, self.signup_login_success)
