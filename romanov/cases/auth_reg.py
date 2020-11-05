import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from romanov.steps.auth import Steps

from romanov.app.driver import connect
import datetime


class AuthRegTest(unittest.TestCase):
    seconds_since_epoch = "".join(str(datetime.datetime.now().timestamp()).split('.'))
    regEmail = seconds_since_epoch + 'z@mail.ru'
    regLogin = seconds_since_epoch + 'z'
    regPass = '123456'

    def test_auth_reg_success(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail,  self.regLogin, self.regPass)
        auth.reg()

    def test_auth_reg_underline_login(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  self.regLogin + '_', self.regPass)
        auth.click_reg()
        auth.find_info_error()

    def test_auth_reg_empty_login(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  '', self.regPass)
        auth.click_reg()
        auth.find_info_error()

    def test_auth_reg_empty_pass(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  self.regLogin + '321', '')
        auth.click_reg()
        auth.find_info_error()

    def test_auth_reg_empty_email(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data('',  self.regLogin + '321', self.regPass)
        auth.click_reg()
        auth.find_info_error()

    def test_auth_reg_no_domain_email(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data('email@',  self.regLogin + '321', self.regPass)
        auth.click_reg()
        auth.find_info_error()

    def test_auth_reg_cyrillic_email(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data('почта@маил.ру',  self.regLogin + '321', self.regPass)
        auth.click_reg()
        auth.find_info_error()

    def test_auth_reg_short_login(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  '12', self.regPass)
        auth.click_reg()
        auth.find_info_error()

    def test_auth_reg_cyrillic_login(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  'заяц', self.regPass)
        auth.click_reg()
        auth.find_info_error()

    def test_auth_reg_short_pass(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  self.regLogin + '321', '123')
        auth.click_reg()
        auth.find_info_error()

    def test_auth_reg_exist_email(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data('test@test.ru',  self.regLogin + '321', self.regPass)
        auth.click_reg()
        auth.find_info_error()

    def test_auth_reg_exist_login(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data('tes32t@te23st.ru', 'test', self.regPass)
        auth.click_reg()
        auth.find_info_error()

    def test_auth_reg_refresh_page(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'rt', self.regLogin + 'rt', self.regPass)
        auth.reg()
        auth.open_app()
        auth.find_auth_menu()