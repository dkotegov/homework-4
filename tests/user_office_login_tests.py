# -*- coding: utf-8 -*-

import os
import random
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.admin_page import AdminPage
from tests.pages.user_page import UserPage


class UserOfficeLoginTests(unittest.TestCase):
    USER_NAME = "userMaxim"
    USER_PASSWORD = "qwerty123"

    HTML_TAG = '<script>alert("alert")</script>'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.admin_page = AdminPage(self.driver)
        self.admin_page.open()
        self.admin_page.add_user(self.USER_NAME, self.USER_PASSWORD)

        self.user_page = UserPage(self.driver)
        self.user_page.open()

        self.login_form = self.user_page.login_form

    def tearDown(self):
        self.admin_page.open()
        self.admin_page.reset()
        self.driver.quit()

    def test_login_form_valid_all(self):
        self.login_form.set_login(self.USER_NAME)
        self.login_form.set_password(self.USER_PASSWORD)
        self.login_form.submit()

        self.user_page.wait_office_login()

        current_login = self.user_page.get_user_info_login()

        self.assertEqual(current_login, self.USER_NAME)

    def test_login_form_empty_login(self):
        self.login_form.set_login("")
        self.login_form.set_password(self.USER_PASSWORD)
        self.login_form.submit()

        alert_text = self.user_page.alert_accept()

        self.assertEqual(alert_text, self.login_form.get_empty_login_msg())

    def test_login_form_empty_password(self):
        self.login_form.set_login(self.USER_NAME)
        self.login_form.set_password("")
        self.login_form.submit()

        alert_text = self.user_page.alert_accept()

        self.assertEqual(alert_text, self.login_form.get_empty_password_msg())

    def test_login_form_html_injection_login(self):
        self.login_form.set_login(self.HTML_TAG + self.USER_NAME)
        self.login_form.set_password(self.USER_PASSWORD)
        self.login_form.submit()

        alert_text = self.user_page.alert_accept()

        self.assertEqual(alert_text, self.login_form.get_invalid_login_msg())

    def test_login_form_html_injection_password(self):
        self.login_form.set_login(self.USER_NAME)
        self.login_form.set_password(self.HTML_TAG + self.USER_NAME)
        self.login_form.submit()

        alert_text = self.user_page.alert_accept()

        self.assertEqual(alert_text, self.login_form.get_invalid_password_msg())

    def test_login_form_auth_err(self):
        self.login_form.set_login("login" + self.USER_NAME)
        self.login_form.set_password("pswd" + self.USER_PASSWORD)
        self.login_form.submit()

        alert_text = self.user_page.alert_accept()

        self.assertEqual(alert_text, self.login_form.get_auth_err_msg())

    def test_login_form_auth_login_err(self):
        self.login_form.set_login("login" + self.USER_NAME)
        self.login_form.set_password(self.USER_PASSWORD)
        self.login_form.submit()

        alert_text = self.user_page.alert_accept()

        self.assertEqual(alert_text, self.login_form.get_auth_err_msg())

    def test_login_form_auth_pswd_err(self):
        self.login_form.set_login(self.USER_NAME)
        self.login_form.set_password("pswd" + self.USER_PASSWORD)
        self.login_form.submit()

        alert_text = self.user_page.alert_accept()

        self.assertEqual(alert_text, self.login_form.get_auth_err_msg())
