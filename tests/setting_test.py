import os

import unittest
from selenium import webdriver
import urllib.parse as urlparse
import time
from Pages.auth_page import AuthPage
from Pages.settings_page import SettingPage
from Pages.profile_page import ProfilePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities, Remote


class SettingsTests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_change_password(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        setting_page = SettingPage(self.driver)
        setting_page.open()
        new_pass = "new_password"
        setting_page.change_pass(setting_page.PASSWORD_INPUT, new_pass, new_pass)
        auth_page.logout()
        auth_page.open()
        auth_page.PASSWORD_INPUT = new_pass
        auth_page.auth()
        setting_page.open()
        setting_page.change_pass(new_pass, setting_page.PASSWORD_INPUT, setting_page.PASSWORD_INPUT)

    def test_change_password_wrong_old(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        setting_page = SettingPage(self.driver)
        setting_page.open()
        new_pass = "new_password"
        setting_page.change_pass(setting_page.PASSWORD_INPUT+"1", new_pass, new_pass)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, setting_page.ERROR_WRONG_OLD)))

    def test_change_password_different_new(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        setting_page = SettingPage(self.driver)
        setting_page.open()
        new_pass = "new_password"
        setting_page.change_pass(setting_page.PASSWORD_INPUT, new_pass, new_pass+"1")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, setting_page.ERROR_DIFF_NEW)))

    def test_change_username(self):
        profile_page = ProfilePage(self.driver)
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        setting_page = SettingPage(self.driver)
        setting_page.open()
        new_username = setting_page.SIGNUP_LOGIN
        setting_page.change_username(new_username)
        check = profile_page.check_username(new_username)
        setting_page.open()
        setting_page.change_username(setting_page.USERNAME_INPUT)
        self.assertEqual(check, True)

    def test_change_username_less_5(self):
        profile_page = ProfilePage(self.driver)
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        setting_page = SettingPage(self.driver)
        setting_page.open()
        new_username = "1234"
        setting_page.change_username(new_username)
        self.assertEqual(profile_page.check_username(new_username), False)

    def test_change_username_exist(self):
        profile_page = ProfilePage(self.driver)
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        setting_page = SettingPage(self.driver)
        setting_page.open()
        new_username = "testErik"
        setting_page.change_username(new_username)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, setting_page.ERROR_USERNAME_EXIST)))





