import unittest

from pages.auth_page import AuthPage
from pages.registration_page import RegistrationPage
from scenario.auth import setup_auth
from scenario.default_setup import default_setup


class CheckAuth(unittest.TestCase):
    incorrect_password = 'q'
    invalid_password = 'margarita'
    incorrect_email = 'margot.ru'
    invalid_email = 'margot1@margot1.ru'
    correct_email = 'margot@margot.ru'
    correct_password = 'margot'

    invalid_password_data = {
        'EMAIL': correct_email,
        'PASSWORD': invalid_password
    }

    short_password_data = {
        'EMAIL': correct_email,
        'PASSWORD': incorrect_password
    }

    invalid_email_data = {
        'EMAIL': invalid_email,
        'PASSWORD': correct_password
    }

    incorrect_email_data = {
        'EMAIL': incorrect_email,
        'PASSWORD': correct_password
    }

    empty_fields_data = {
        'EMAIL': '',
        'PASSWORD': ''
    }

    empty_email_data = {
        'EMAIL': '',
        'PASSWORD': correct_password
    }

    empty_password_data = {
        'EMAIL': correct_email,
        'PASSWORD': ''
    }

    def setUp(self) -> None:
        default_setup(self)

        self.auth_page = AuthPage(self.driver)
        self.reg_page = RegistrationPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_to_registration(self):
        self.auth_page.open()
        self.auth_page.go_to_reg()
        self.reg_page.is_open()

    def test_success_auth(self):
        self.assertTrue(setup_auth(self))

    def test_invalid_password(self):
        setup_auth(self, self.invalid_password_data)
        self.assertTrue(self.auth_page.top_error())

    def test_invalid_email(self):
        setup_auth(self, self.invalid_email_data)
        self.assertTrue(self.auth_page.top_error())

    def test_incorrect_password(self):
        setup_auth(self, self.short_password_data)
        self.assertTrue(self.auth_page.password_error('Пароль должен содержать по крайней мере от 5 до 25 символов.'))

    def test_incorrect_email(self):
        setup_auth(self, self.incorrect_email_data)
        self.assertTrue(self.auth_page.email_error('Email должен содержать "@" и латинские буквы, цифры, символы.'))

    def test_empty_fields(self):
        setup_auth(self, self.empty_fields_data)
        self.assertTrue(self.auth_page.empty_fields())

    def test_empty_email(self):
        setup_auth(self, self.empty_email_data)
        self.assertTrue(self.auth_page.email_error('Укажите email.'))

    def test_empty_password(self):
        setup_auth(self, self.empty_password_data)
        self.assertTrue(self.auth_page.password_error('Укажите пароль.'))

