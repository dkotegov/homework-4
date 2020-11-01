import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.login_page import LoginPage


class LoginPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()

        login_form = login_page.login_form

        login = os.environ.get('LOGIN')
        login_form.set_login(login)

        password = os.environ.get('PASSWORD')
        login_form.set_password(password)

        login_form.submit()

        nickname = login_page.main_header.get_nickname()
        self.assertEqual(login, nickname)


