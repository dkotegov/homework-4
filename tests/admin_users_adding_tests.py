# -*- coding: utf-8 -*-

import os
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.admin_page import AdminPage


class AdminUsersAddingTests(unittest.TestCase):
    HTML_TAG = '<script>alert("alert")</script>'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')  # use
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.admin_page = AdminPage(self.driver)
        self.admin_page.open()
        self.admin_page.goto_user_form()
        self.user_form = self.admin_page.user_form
        self.user_list = self.admin_page.user_list

    def tearDown(self):
        self.admin_page.reset()
        self.driver.quit()

    def test_form_empty_all(self):
        self.user_form.set_login("")
        self.user_form.set_password("")
        self.user_form.submit()
        alert_text = self.admin_page.alert_accept()
        self.assertEqual(alert_text.encode('utf-8'), self.user_form.get_empty_login_msg())

    def test_form_empty_login(self):
        self.user_form.set_login("")
        self.user_form.set_password("qwerty123")
        self.user_form.submit()
        alert_text = self.admin_page.alert_accept()
        self.assertEqual(alert_text.encode('utf-8'), self.user_form.get_empty_login_msg())

    def test_form_empty_password(self):
        self.user_form.set_login("maxim123")
        self.user_form.set_password("")
        self.user_form.submit()
        alert_text = self.admin_page.alert_accept()
        self.assertEqual(alert_text.encode('utf-8'), self.user_form.get_empty_password_msg())

    def test_form_invalid_login(self):
        self.user_form.set_login(self.HTML_TAG + "maxim")
        self.user_form.set_password("qwerty123")
        self.user_form.submit()
        alert_text = self.admin_page.alert_accept()
        self.assertEqual(alert_text.encode('utf-8'), self.user_form.get_invalid_login_msg())

    def test_form_invalid_password(self):
        self.user_form.set_login("maxim")
        self.user_form.set_password(self.HTML_TAG + "qwerty123")
        self.user_form.submit()
        alert_text = self.admin_page.alert_accept()
        self.assertEqual(alert_text.encode('utf-8'), self.user_form.get_invalid_password_msg())

    def test_form_invalid_all(self):
        self.user_form.set_login(self.HTML_TAG + "maxim")
        self.user_form.set_password(self.HTML_TAG + "qwerty123")
        self.user_form.submit()
        alert_text = self.admin_page.alert_accept()
        self.assertEqual(alert_text.encode('utf-8'), self.user_form.get_invalid_login_msg())

    def test_form_valid_all(self):
        self.user_form.set_login("maxim12345")
        self.user_form.set_password("qwerty123")
        self.user_form.submit()
        alert_text = self.admin_page.alert_accept()
        self.assertEqual(alert_text.encode('utf-8'), self.user_form.get_ok_msg())

    def test_form_already_exists(self):
        self.user_form.set_login("user123")
        self.user_form.set_password("qwerty123")
        self.user_form.submit()
        self.admin_page.alert_accept()

        self.user_form.clear_login()
        self.user_form.clear_password()
        self.user_form.set_login("user123")
        self.user_form.set_password("qwerty123")
        self.user_form.submit()
        alert_text = self.admin_page.alert_accept()

        self.assertEqual(alert_text.encode('utf-8'), self.user_form.get_already_exists_msg())

    def test_add_user_to_base(self):
        self.admin_page.goto_user_list()
        start_count = self.user_list.count_records()

        self.admin_page.goto_user_form()
        self.user_form.set_login("user123")
        self.user_form.set_password("qwerty123")
        self.user_form.submit()
        self.admin_page.alert_accept()

        self.admin_page.goto_user_list()
        current_count = self.user_list.count_records()

        self.assertEqual(current_count, start_count + 1)