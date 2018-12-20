# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.admin_page import AdminPage
from tests.pages.user_page import UserPage


class UserOfficeColorThemeTests(unittest.TestCase):
    USER_NAME = "userMaxim"
    USER_PASSWORD = "qwerty123"

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')  # use
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.admin_page = AdminPage(self.driver)
        self.admin_page.open()
        self.admin_page.add_user(self.USER_NAME, self.USER_PASSWORD)

        self.user_page = UserPage(self.driver)
        self.user_page.open()

        self.user_page.sign_in(self.USER_NAME, self.USER_PASSWORD)

        self.color_changer = self.user_page.color_changer

    def tearDown(self):
        self.admin_page.open()
        self.admin_page.reset()
        self.driver.quit()

    def test_background_color_change(self):
        start_color = self.color_changer.get_background_color()
        self.color_changer.click_color_change_btn_last()
        current_color = self.color_changer.get_background_color()
        self.assertNotEqual(current_color, start_color)

    def test_save_theme_to_localstorage(self):
        start_color = self.color_changer.get_color_from_localstorage()
        self.color_changer.click_color_change_btn_last()
        current_color = self.color_changer.get_color_from_localstorage()
        self.assertNotEqual(current_color, start_color)
