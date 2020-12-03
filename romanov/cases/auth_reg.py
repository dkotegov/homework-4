import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from romanov.steps.auth import Steps

from romanov.app.driver import connect
import datetime

GOOD_REG = "Регистрация завершена!\nДобро пожаловать!"
ERR_REG = "Ошибка регистрации"
ERR_LOG = "Логин должен состоять из трех и более символов,\nи содержать только латинские буквы, цифры и подчеркивание"
ERR_PASS = "Пароль должен состоять из шести или более символов"
ERR_EMAIL = "Введите корректный email"
EXIST_EMAIL = "Пользователь с такой почтой уже есть"
EXIST_LOG = "Пользователь с таким логином уже есть"
EMPTY = ""

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
        res = auth.reg()
        self.assertEqual(res, GOOD_REG)

    def test_auth_reg_underline_login(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  self.regLogin + '_', self.regPass)
        auth.click_reg()
        res = auth.find_info_error()
        self.assertEqual(res, ERR_REG)

    def test_auth_reg_empty_login(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  '', self.regPass)
        auth.click_reg()
        res = auth.find_info_error()
        self.assertEqual(res, ERR_LOG)

    def test_auth_reg_empty_pass(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  self.regLogin + '321', '')
        auth.click_reg()
        res = auth.find_info_error()
        self.assertEqual(res, ERR_PASS)

    def test_auth_reg_empty_email(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data('',  self.regLogin + '321', self.regPass)
        auth.click_reg()
        res = auth.find_info_error()
        self.assertEqual(res, ERR_EMAIL)

    def test_auth_reg_no_domain_email(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data('email@',  self.regLogin + '321', self.regPass)
        auth.click_reg()
        res = auth.find_info_error()
        self.assertEqual(res, ERR_EMAIL)

    def test_auth_reg_cyrillic_email(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data('почта@маил.ру',  self.regLogin + '321', self.regPass)
        auth.click_reg()
        res = auth.find_info_error()
        self.assertEqual(res, ERR_EMAIL)

    def test_auth_reg_short_login(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  '12', self.regPass)
        auth.click_reg()
        res = auth.find_info_error()
        self.assertEqual(res, ERR_LOG)

    def test_auth_reg_cyrillic_login(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  'заяц', self.regPass)
        auth.click_reg()
        res = auth.find_info_error()
        self.assertEqual(res, ERR_LOG)

    def test_auth_reg_short_pass(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'ru',  self.regLogin + '321', '123')
        auth.click_reg()
        res = auth.find_info_error()
        self.assertEqual(res, ERR_PASS)

    def test_auth_reg_exist_email(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data('test@test.ru',  self.regLogin + '321', self.regPass)
        auth.click_reg()
        res = auth.find_info_error()
        self.assertEqual(res, EXIST_EMAIL)

    def test_auth_reg_exist_login(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data('tes32t@te23st.ru', 'test', self.regPass)
        auth.click_reg()
        res = auth.find_info_error()
        self.assertEqual(res, EXIST_LOG)

    def test_auth_reg_refresh_page(self):
        auth = Steps()
        auth.open_app()
        auth.open_reg()
        auth.enter_reg_data(self.regEmail + 'rt', self.regLogin + 'rt', self.regPass)
        auth.reg()
        auth.open_app()
        res = auth.find_auth_menu()
        self.assertNotEqual(res, EMPTY)
