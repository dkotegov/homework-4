# -*- coding: utf-8 -*-
from BasicTest import BasicTest

from pages.LoginPage import LoginPage


class LoginTest(BasicTest):
    def setUp(self):
        super(LoginTest, self).setUp()
        self.login_page = LoginPage(self.driver)
        self.login_page.open()

    def test_correct_login(self):
        self.login_page.sign_in(self.login, self.password)
        self.login_page.wait_redirect(self.MAIL_URL)

    def test_wrong_password(self):
        wrong_password = 'wrongpassword'
        self.login_page.sign_in(self.login, wrong_password)
        test_validation = self.login_page.get_valigation_message()
        expected_validation = 'Неверный пароль, попробуйте ещё раз'
        self.assertEqual(test_validation, expected_validation)

    def test_empty_password(self):
        empty_password = ''
        self.login_page.sign_in(self.login, empty_password)
        test_validation = self.login_page.get_valigation_message()
        expected_validation = 'Поле «Пароль» должно быть заполнено'
        self.assertEqual(test_validation, expected_validation)
