# -*- coding: utf-8 -*-
import os
import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from config import config

from pages.LoginPage import LoginPage


class BasicTest(unittest.TestCase):
    MAIL_URL = 'https://e.mail.ru/inbox'
    LOGIN_URL = 'https://account.mail.ru/login'
    AUTH_URL = 'https://e.mail.ru/login'
    SIGNUP_URL = 'https://account.mail.ru/signup'
    SETTINGS_URL = 'https://e.mail.ru/settings/userinfo'
    MAIN_PAGE_URL = 'https://mail.ru'

    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')

    def setUp(self):
        if (config.ON_DRIVER):
            self.driver = webdriver.Chrome(config.DRIVER)
        else:
            nodeUrl = 'http://localhost:4444/wd/hub'
            self.driver = webdriver.Remote(
                command_executor = nodeUrl,
                desired_capabilities = {
                    'browserName': config.BROWSER,
                }
            )
            # self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def auth(self):
        login_page = LoginPage(self.driver)
        login_page.sign_in(self.login, self.password)
        login_page.wait_redirect(self.MAIL_URL)
