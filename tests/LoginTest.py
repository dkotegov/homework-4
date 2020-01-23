# -*- coding: utf-8 -*-
from BasicTest import BasicTest

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage

import time


class LoginTest(BasicTest):

    def setUp(self):
        super(LoginTest, self).setUp()
        self.login_page = LoginPage(self.driver)
        self.login_page.open()
        self.main_page = MainPage(self.driver)

    def test_correct_login(self):
        self.login_page.sign_in(self.login, self.password)
        self.login_page.wait_redirect(self.MAIL_URL)

    def test_wrong_password(self):
        wrong_password = 'wrongpassword'
        self.login_page.sign_in(self.login, wrong_password)
        test_validation = self.login_page.get_validation_message()
        expected_validation1 = 'Неверный пароль, попробуйте ещё раз'
        expected_validation2 = 'Incorrect password. Try again'
        self.assertIn(test_validation, [
                      expected_validation1, expected_validation2])

    def test_yandex_login(self):
        test_login = '123@yandex.ru'
        self.login_page.enter_login(test_login)
        self.login_page.click_continue()
        self.login_page.wait_redirect('https://passport.yandex.ru/auth')

    def test_gmail_login(self):
        test_login = '123@gmail.com'
        self.login_page.enter_login(test_login)
        self.login_page.click_continue()
        self.login_page.wait_redirect(
            'https://accounts.google.com/signin/oauth/identifier')

    def test_yahoo_login(self):
        test_login = '123@yahoo.com'
        self.login_page.enter_login(test_login)
        self.login_page.click_continue()
        self.login_page.wait_redirect('https://login.yahoo.com/')

    def test_rambler_login(self):
        test_login = '123@rambler.ru'
        self.login_page.sign_in(test_login, self.password)
        err = self.login_page.get_protocol_err()
        expected_err1 = 'Вы можете добавить любой почтовый ящик, поддерживающий сбор почты по протоколу POP/IMAP. Если логин введен неверно, авторизуйтесь заново.'
        expected_err2 = 'You can add any mailbox that supports POP/IMAP. If your credentials were entered incorrectly, sign in again.'
        self.assertIn(err, [expected_err1, expected_err2])

    def test_custom_login(self):
        custom_login = 'custom@petrov.ru'
        custom_password = 'customPassword123'
        self.login_page.sign_in(custom_login, custom_password)
        err = self.login_page.get_domain_err()
        possible_errors = [
            'Try again later.',
            'Повторите попытку через некоторое время.',
            'Произошла ошибка! Пожалуйста, повторите попытку через некоторое время или введите имя и пароль другого аккаунта.',
            'You can add any mailbox that supports POP/IMAP. If your credentials were entered incorrectly, sign in again.',
        ]
        self.assertIn(err, possible_errors)

    def test_empty_password(self):
        empty_password = ''
        self.login_page.sign_in(self.login, empty_password)
        test_validation = self.login_page.get_validation_message()
        expected_validation1 = 'Поле «Пароль» должно быть заполнено'
        expected_validation2 = 'The "Password" field is required'
        self.assertIn(test_validation, [
                      expected_validation1, expected_validation2])

    def test_signout(self):
        self.login_page.sign_in(self.login, self.password)
        self.login_page.wait_redirect(self.MAIL_URL)
        self.main_page.click_signout()
        self.main_page.wait_redirect(self.MAIN_PAGE_URL)
