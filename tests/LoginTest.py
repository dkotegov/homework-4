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
        MAIL_URL = self.MAIL_URL + '/'
        self.login_page.sign_in(self.login, self.password)
        self.login_page.wait_redirect(MAIL_URL)
        self.assertEqual(self.driver.current_url.split('?')[0], MAIL_URL)

    def test_wrong_password(self):
        WRONG_PASSWORD = 'wrongpassword'
        self.login_page.sign_in(self.login, WRONG_PASSWORD)
        test_validation = self.login_page.get_validation_message()
        EXPECTED_VALIDATION_1 = 'Неверный пароль, попробуйте ещё раз'
        EXPECTED_VALIDATION_2 = 'Incorrect password. Try again'
        self.assertIn(test_validation, [EXPECTED_VALIDATION_1, EXPECTED_VALIDATION_2])

    def test_yandex_login(self):
        TEST_LOGIN = '1gere23@yandex.ru'
        PASSWORD_YANDEX_URL = 'https://passport.yandex.ru/auth'
        self.login_page.enter_login(TEST_LOGIN)
        self.login_page.click_continue()
        self.login_page.wait_redirect(PASSWORD_YANDEX_URL)
        self.assertEqual(self.driver.current_url.split('?')[0], PASSWORD_YANDEX_URL)

    def test_gmail_login(self):
        TEST_LOGIN = '1wqx23@gmail.com'
        GOOGLE_ACCOUNT_URL = 'https://accounts.google.com/signin/oauth/identifier'
        self.login_page.enter_login(TEST_LOGIN)
        self.login_page.click_continue()
        self.login_page.wait_redirect(GOOGLE_ACCOUNT_URL)
        self.assertEqual(self.driver.current_url.split('?')[0], GOOGLE_ACCOUNT_URL)

    def test_yahoo_login(self):
        TEST_LOGIN = '1sad3@yahoo.com'
        YAHOO_ACCOUNT_URL = 'https://login.yahoo.com/'
        self.login_page.enter_login(TEST_LOGIN)
        self.login_page.click_continue()
        self.login_page.wait_redirect(YAHOO_ACCOUNT_URL)
        self.assertEqual(self.driver.current_url.split('?')[0], YAHOO_ACCOUNT_URL)

    def test_rambler_login(self):
        TEST_LOGIN = '2DSA3@rambler.ru'
        self.login_page.sign_in(TEST_LOGIN, self.password)
        err = self.login_page.get_protocol_err()
        EXPECTED_ERR_1 = 'Вы можете добавить любой почтовый ящик, поддерживающий сбор почты по протоколу POP/IMAP. Если логин введен неверно, авторизуйтесь заново.'
        EXPECTED_ERR_2 = 'You can add any mailbox that supports POP/IMAP. If your credentials were entered incorrectly, sign in again.'
        self.assertIn(err, [EXPECTED_ERR_1, EXPECTED_ERR_2])

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
        self.assertIn(test_validation, [EXPECTED_VALIDATION_1, EXPECTED_VALIDATION_2])

    def test_signout(self):
        self.login_page.sign_in(self.login, self.password)
        self.login_page.wait_redirect(self.MAIL_URL)
        self.main_page.click_signout()
        self.main_page.wait_redirect(self.MAIN_PAGE_URL)
        self.assertEqual(self.driver.current_url.split('?')[0], self.MAIN_PAGE_URL)
