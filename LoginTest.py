import os
import unittest
import config
from LoginPage import LoginPage

from selenium import webdriver


class LoginTest(unittest.TestCase):
    BASE_URL = 'https://m.calendar.mail.ru/'
    AUTH_URL = 'https://e.mail.ru/login'
    ACCOUNT_URL = 'https://account.mail.ru/'
    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')

    def setUp(self):
        self.driver = webdriver.Chrome(config.DRIVER)

    def tearDown(self):
        self.driver.quit()

    def test_correct_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_login(self.login)
        login_page.enter_password(self.password)
        login_page.login()
        login_page.wait_redirect(self.BASE_URL)

    def test_incorrect_password(self):
        wrong_password = 'wrongpassword'
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_login(self.login)
        login_page.enter_password(wrong_password)
        login_page.login()
        login_page.wait_redirect(self.AUTH_URL)

    def test_incorrect_email(self):
        wrong_email = 'yandex.ru'
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_login(wrong_email)
        login_page.enter_password(self.password)
        login_page.login()
        login_page.email_required()

    def test_empty_fields(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        login_page.email_required()

    def test_forgot_password(self):
        login_page = LoginPage(self.driver)
        login_page.forgot_password()
        login_page.wait_redirect(self.ACCOUNT_URL)

    def test_register(self):
        login_page = LoginPage(self.driver)
        login_page.register()
        login_page.wait_redirect(self.ACCOUNT_URL)
