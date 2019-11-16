import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

from LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_correct_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_login(self.login)
        login_page.enter_password(self.password)
        login_page.login()
        login_page.wait_redirect('https://m.calendar.mail.ru/')

    def test_incorrect_password(self):
        wrong_password = 'wrong-password'
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_login(self.login)
        login_page.enter_password(wrong_password)
        login_page.login()

    def test_incorrect_email(self):
        wrong_email = 'mymail@yandex.ru'
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_login(wrong_email)
        login_page.enter_password(self.password)
        login_page.login()

    def test_empty_fields(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        login_page.wait_redirect('https://e.mail.ru/login/')

    def test_forgot_password(self):
        login_page = LoginPage(self.driver)
        login_page.forgot_password()
        login_page.wait_redirect('https://account.mail.ru/recovery/')

    def test_register(self):
        login_page = LoginPage(self.driver)
        login_page.register()
        login_page.wait_redirect('https://account.mail.ru/signup/')
