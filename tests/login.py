import os
import unittest

from pages.login import LoginPage
from selenium.webdriver import DesiredCapabilities, Remote


class LoginTest(unittest.TestCase):

    USERNAME = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = LoginPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()
        hello_msg = auth_form.get_hello_msg()
        true_hello_msg = auth_form.get_true_hello_msg()
        self.assertEqual(hello_msg, true_hello_msg)



    def loginBeforeAllTests(self, second_profile=False):
        USERNAME = os.environ['LOGIN']
        PASSWORD = os.environ['PASSWORD']
        if second_profile:
            USERNAME = os.environ['LOGIN2']
            PASSWORD = os.environ['PASSWORD2']

        auth_page = LoginPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()
        hello_msg = auth_form.get_hello_msg()
        true_hello_msg = auth_form.get_true_hello_msg()
        self.assertEqual(hello_msg, true_hello_msg)
        self.driver.refresh()
