# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.admin_page import AdminPage


class AdminUsersAddingTests(unittest.TestCase):
    HTML_TAG = '<script>alert("alert")</script>'

    get_ok_msg = "Добавление пользователя прошло успешно."
    get_empty_login_msg = "Пустой логин."
    get_empty_password_msg = "Пустой пароль."
    get_invalid_login_msg = "Некорректный логин."
    get_invalid_password_msg = "Некорректный пароль."
    get_already_exists_msg = "Пользователь уже существует в базе данных."

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
        alert_text = self.admin_page.add_user("", "")
        self.assertEqual(alert_text, self.get_empty_login_msg)

    def test_form_empty_login(self):
        alert_text = self.admin_page.add_user(name="", password="qwerty123")
        self.assertEqual(alert_text, self.get_empty_login_msg)

    def test_form_empty_password(self):
        alert_text = self.admin_page.add_user(name="maxim", password="")
        self.assertEqual(alert_text, self.get_empty_password_msg)

    def test_form_invalid_login(self):
        alert_text = self.admin_page.add_user(
            name=self.HTML_TAG + "maxim",
            password="qwerty123")
        self.assertEqual(alert_text, self.get_invalid_login_msg)

    def test_form_invalid_password(self):
        alert_text = self.admin_page.add_user(
            name="maxim",
            password=self.HTML_TAG + "qwerty123")
        self.assertEqual(alert_text, self.get_invalid_password_msg)

    def test_form_invalid_all(self):
        alert_text = self.admin_page.add_user(
            name=self.HTML_TAG + "maxim",
            password=self.HTML_TAG + "qwerty123")
        self.assertEqual(alert_text, self.get_invalid_login_msg)

    def test_form_valid_all(self):
        alert_text = self.admin_page.add_user(
            name="maxim",
            password="qwerty123")
        self.assertEqual(alert_text, self.get_ok_msg)

    def test_form_already_exists(self):
        self.admin_page.add_user(
            name="maxim",
            password="qwerty123")
        alert_text = self.admin_page.add_user(
            name="maxim",
            password="qwerty123")
        self.assertEqual(alert_text, self.get_already_exists_msg)

    def test_add_user_to_base(self):
        self.admin_page.goto_user_list()
        start_count = self.user_list.count_records()

        self.admin_page.add_user(
            name="maxim",
            password="qwerty123")

        self.admin_page.goto_user_list()
        current_count = self.user_list.count_records()

        self.assertEqual(current_count, start_count + 1)
