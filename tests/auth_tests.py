import os

import unittest
from selenium import webdriver
import urllib.parse as urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from Pages.auth_page import AuthPage


class AuthTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_auth_succes(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()

    def test_auth_wrong_login(self):
        auth_page = AuthPage(self.driver)
        password = os.environ['PASSWORD']
        auth_page.auth_wrong("xmksamxsmlksa", password)

    def test_auth_wrong_password(self):
        auth_page = AuthPage(self.driver)
        login = os.environ['LOGIN']
        auth_page.auth_wrong(login, "ofcspslaxx")

    def test_auth_clear(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth_wrong("", "")

    def test_logout(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        auth_page.logout()
