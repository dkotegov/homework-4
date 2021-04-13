import os

import unittest
from selenium import webdriver
import urllib.parse as urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from Pages.signup_page import SignupPage


class SignupTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

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
