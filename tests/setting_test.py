import os

import unittest
from selenium import webdriver
import urllib.parse as urlparse
import time

from Pages.auth_page import AuthPage
from Pages.settings_page import SettingPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SettingsTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

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
