# -*- coding: utf-8 -*-
from BasicTest import BasicTest

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage


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
        WRONG_PASSWORD = 'wrongpassword'
        self.login_page.sign_in(self.login, WRONG_PASSWORD)
        test_validation = self.login_page.get_validation_message()
        EXPECTED_VALIDATION_1 = 'Неверный пароль, попробуйте ещё раз'
        EXPECTED_VALIDATION_2 = 'Incorrect password. Try again'
        self.assertIn(test_validation, [
                      EXPECTED_VALIDATION_1, EXPECTED_VALIDATION_2])

    def test_yandex_login(self):
        TEST_LOGIN = '123@yandex.ru'
        self.login_page.enter_login(TEST_LOGIN)
        self.login_page.click_continue()
        self.login_page.wait_redirect('https://passport.yandex.ru/auth')

    def test_gmail_login(self):
        TEST_LOGIN = '123@gmail.com'
        self.login_page.enter_login(TEST_LOGIN)
        self.login_page.click_continue()
        self.login_page.wait_redirect(
            'https://accounts.google.com/signin/oauth/identifier')

    def test_yahoo_login(self):
        TEST_LOGIN = '123@yahoo.com'
        self.login_page.enter_login(TEST_LOGIN)
        self.login_page.click_continue()
        self.login_page.wait_redirect('https://login.yahoo.com/')

    def test_rambler_login(self):
        TEST_LOGIN = '2Q3@rambler.ru'
        self.login_page.sign_in(TEST_LOGIN, self.password)
        err = self.login_page.get_protocol_err()
        expected_err1 = 'Вы можете добавить любой почтовый ящик, поддерживающий сбор почты по протоколу POP/IMAP. Если логин введен неверно, авторизуйтесь заново.'
        expected_err2 = 'You can add any mailbox that supports POP/IMAP. If your credentials were entered incorrectly, sign in again.'
        self.assertIn(err, [expected_err1, expected_err2])

    def test_custom_login(self):
        CUSTOM_LOGIN = 'custom@petrov.ru'
        CUSTOM_PASSWORD = 'customPassword123'
        self.login_page.sign_in(CUSTOM_LOGIN, CUSTOM_PASSWORD)
        err = self.login_page.get_domain_err()
        POSSIBLE_ERRORS = [
            'Try again later.',
            'Повторите попытку через некоторое время.',
            'Произошла ошибка! Пожалуйста, повторите попытку через некоторое время или введите имя и пароль другого аккаунта.',
            'You can add any mailbox that supports POP/IMAP. If your credentials were entered incorrectly, sign in again.',
        ]
        self.assertIn(err, POSSIBLE_ERRORS)

    def test_empty_password(self):
        EMPTY_PASSWORD = ''
        self.login_page.sign_in(self.login, EMPTY_PASSWORD)
        test_validation = self.login_page.get_validation_message()
        EXPECTED_VALIDATION_1 = 'Поле «Пароль» должно быть заполнено'
        EXPECTED_VALIDATION_2 = 'The "Password" field is required'
        self.assertIn(test_validation, [
                      EXPECTED_VALIDATION_1, EXPECTED_VALIDATION_2])

    def test_signout(self):
        self.login_page.sign_in(self.login, self.password)
        self.login_page.wait_redirect(self.MAIL_URL)
        self.main_page.click_signout()
        self.main_page.wait_redirect(self.MAIN_PAGE_URL)
