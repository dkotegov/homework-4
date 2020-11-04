import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.login_page import LoginPage
from pages.join_page import JoinPage


class LoginPageTest(unittest.TestCase):
    login_page = None

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

        self.login_page = LoginPage(self.driver)
        self.login_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_success_login(self):
        login = os.environ.get('LOGIN')
        password = os.environ.get('PASSWORD')

        is_login = self.login_page.login(login, password)

        self.assertTrue(is_login)

    def test_invalid_login(self):
        login = '123'
        password = '321'

        self.login_page.login(login, password)

        is_open = self.login_page.login_form.is_open_invalid_login()
        self.assertTrue(is_open)

    def test_empty_inputs_login(self):
        self.login_page.login_form.submit()

        is_open = self.login_page.login_form.is_open_invalid_login()
        self.assertTrue(is_open)

    def test_click_on_join(self):
        self.login_page.login_form.open_join()

        join_form = JoinPage(self.driver).join_form
        self.assertTrue(join_form.is_open)
