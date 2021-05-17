import os

import unittest
from default_setup import default_setup
from selenium import webdriver
import urllib.parse as urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from Pages.signup_page import SignupPage


class SignupTests(unittest.TestCase):
    signup_login_success = "abrikos-molokosos"
    signup_password = "12345678"
    signup_mail = "qwer@mail.ru"

    def setUp(self):
        default_setup(self)
        self.signup_page = SignupPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_signup_succes(self):
        signup_page = SignupPage(self.driver)
        login = signup_page.SIGNUP_LOGIN
        signup_page.signup(login, "12345678", "qwer@mail.ru")

    def test_signup_exist_login(self):
        signup_page = SignupPage(self.driver)
        login = os.environ['LOGIN']
        signup_page.signup_wrong(login, "12345678", "qwer@mail.ru")

    def test_signup_login_less_5_symbols(self):
        signup_page = SignupPage(self.driver)
        signup_page.signup_wrong("qqqq", "12345678", "qwer@mail.ru")

    def test_signup_pass_less_8_symbols(self):
        signup_page = SignupPage(self.driver)
        signup_page.signup_wrong("axsaxsaxxs", "1234567", "qwer@mail.ru")

    def test_signup_clear(self):
        signup_page = SignupPage(self.driver)
        signup_page.signup_wrong("", "", "")
