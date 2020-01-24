# -*- coding: utf-8 -*-
import os
import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from config import config

from pages.LoginPage import LoginPage


class BasicTest(unittest.TestCase):
    MAIL_URL = 'https://e.mail.ru/inbox'
    SIGNUP_VERIFY_URL = 'https://account.mail.ru/signup/verify'
    LOGIN_URL = 'https://account.mail.ru/login'
    AUTH_URL = 'https://e.mail.ru/login'
    SIGNUP_URL = 'https://account.mail.ru/signup'
    SETTINGS_URL = 'https://e.mail.ru/settings/userinfo'
    MAIN_PAGE_URL = 'https://mail.ru'
    SIGNUP_USE_CONDITION = 'https://help.mail.ru/legal/terms/mail'

    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')

    login2 = os.environ.get('LOGIN2')
    password2 = os.environ.get('PASSWORD2')

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        if (config.ON_DRIVER):
            self.driver = webdriver.Chrome(config.DRIVER, chrome_options=chrome_options)
        else:
            nodeUrl = 'http://localhost:4444/wd/hub'
            self.driver = webdriver.Remote(
                command_executor=nodeUrl,
                desired_capabilities={
                    'browserName': config.BROWSER,
                },
                chrome_options=chrome_options
            )

    def tearDown(self):
        self.driver.quit()

    def auth(self):
        login_page = LoginPage(self.driver)
        login_page.sign_in(self.login, self.password)
        login_page.wait_redirect(self.MAIL_URL)

    def auth_another_account(self):
        login_page = LoginPage(self.driver)
        login_page.sign_in_only_password(self.password)
        login_page.wait_redirect(self.MAIL_URL)
