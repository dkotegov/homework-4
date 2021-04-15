import unittest

from pages.auth_page import AuthPage
from pages.registration_page import RegistrationPage
from scenario.auth import setup_auth, setup_auth_failed
from tests.default_setup import default_setup


class CheckAuth(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.auth_page = AuthPage(self.driver)
        self.reg_page = RegistrationPage(self.driver)

        self.incorrect_password = 'q'
        self.invalid_password = 'margarita'
        self.incorrect_email = 'margot.ru'
        self.invalid_email = 'margot1@margot1.ru'
        self.correct_email = self.EMAIL_APPL
        self.correct_password = self.PASSWORD_APPL


    def tearDown(self):
        self.driver.quit()

    def test_checkout_to_registration(self):
        self.auth_page.open()
        self.auth_page.go_to_reg()
        self.reg_page.is_open()

    def test_success_auth(self):
        self.assertTrue(setup_auth(self))

    def test_invalid_password(self):
        invalid_password_data = {
            'EMAIL': self.correct_email,
            'PASSWORD': self.invalid_password
        }
        setup_auth_failed(self, invalid_password_data)
        self.assertTrue(self.auth_page.top_error())

    def test_invalid_email(self):
        invalid_email_data = {
            'EMAIL': self.invalid_email,
            'PASSWORD': self.correct_password
        }
        setup_auth_failed(self, invalid_email_data)
        self.assertTrue(self.auth_page.top_error())

    def test_incorrect_password(self):
        short_password_data = {
            'EMAIL': self.correct_email,
            'PASSWORD': self.incorrect_password
        }
        setup_auth_failed(self, short_password_data)
        self.assertTrue(self.auth_page.password_error('Пароль должен содержать по крайней мере от 5 до 25 символов.'))

    def test_incorrect_email(self):
        incorrect_email_data = {
            'EMAIL': self.incorrect_email,
            'PASSWORD': self.correct_password
        }
        setup_auth_failed(self, incorrect_email_data)
        self.assertTrue(self.auth_page.email_error('Email должен содержать "@" и латинские буквы, цифры, символы.'))

    def test_empty_fields(self):
        empty_fields_data = {
            'EMAIL': '',
            'PASSWORD': ''
        }
        setup_auth_failed(self, empty_fields_data)
        self.assertTrue(self.auth_page.empty_fields())

    def test_empty_email(self):
        empty_email_data = {
            'EMAIL': '',
            'PASSWORD': self.correct_password
        }
        setup_auth_failed(self, empty_email_data)
        self.assertTrue(self.auth_page.email_error('Укажите email.'))

    def test_empty_password(self):
        empty_password_data = {
            'EMAIL': self.correct_email,
            'PASSWORD': ''
        }
        setup_auth_failed(self, empty_password_data)
        self.assertTrue(self.auth_page.password_error('Укажите пароль.'))

