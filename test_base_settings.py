# -*- coding: utf-8 -*-

import unittest

import os

import time
from selenium.webdriver import DesiredCapabilities, Remote

from constants import profiles
from pages.auth_page import AuthPage
from pages.base_settings_page import BaseSettingsPage
from pages.main_page import MainPage


class TestsBaseSettings(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()
    #
    # def test_name_surname(self):
    #     name = "Name1"
    #     surname = "Surname1"
    #
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open('')
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)
    #
    #     base_settings_page = BaseSettingsPage(self.driver)
    #     base_settings_page.open('/settings')
    #     personal_data = base_settings_page.personal_data()
    #     personal_data.name_surname(name, surname)
    #     personal_data.save()
    #     personal_data.close_save()
    #
    #     name_surname = base_settings_page.profile_get()
    #     self.assertEqual(name + " " + surname, name_surname)
    #     base_settings_page.profile()
    #
    #     main_page = MainPage(self.driver)
    #     name_surname = main_page.my_name_surname()
    #     self.assertEqual(name + " " + surname, name_surname)

    def test_name_surname_error(self):
        name = "Name_1"
        surname = "Surname_1"
        error = "Пожалуйста, используйте только буквы."

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()

        e1, e2 = personal_data.name_surname_error()

        self.assertEqual(error, e1)
        self.assertEqual(error, e2)







