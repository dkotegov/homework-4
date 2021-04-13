import os

import unittest
from selenium import webdriver
import urllib.parse as urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from Pages.auth_page import AuthPage


class AuthTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_auth_succes(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        auth_page.logout()

    def test_auth_wrong_login(self):
        auth_page = AuthPage(self.driver)
        l = os.environ['LOGIN']
        password = os.environ['PASSWORD']
        login = l + password

