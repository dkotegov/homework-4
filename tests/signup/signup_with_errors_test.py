import os

import constants
from pages.signup import SignupPage
from components.signup_form import SignupForm
from tests.default import Test


class SignUpWithEmptyFieldsTest(Test):
    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = SignupForm(self.driver)
        signup_form.submit()

        self.assertEqual(
            signup_form.get_login_error(),
            constants.ERROR_MSG_OF_EMPTY_SIGNUP_FIELD
        )

        self.assertEqual(
            signup_form.get_email_error(),
            constants.ERROR_MSG_OF_EMPTY_SIGNUP_FIELD
        )

        self.assertEqual(
            signup_form.get_password_error(),
            constants.ERROR_MSG_OF_EMPTY_SIGNUP_FIELD
        )

        self.assertEqual(
            signup_form.get_confirm_password_error(),
            constants.ERROR_MSG_OF_EMPTY_SIGNUP_FIELD
        )


class SignUpWithInvalidLoginTest(Test):
    INVALID_LOGIN = 'Никитосич'
    VALID_EMAIL = 'newemail@mail.ru'

    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = SignupForm(self.driver)
        signup_form.set_login(self.INVALID_LOGIN)
        signup_form.set_email(self.VALID_EMAIL)
        signup_form.set_password(os.environ['PASSWORD'])
        signup_form.set_confirm_password(os.environ['PASSWORD'])
        signup_form.submit()

        self.assertEqual(
            signup_form.get_login_error(),
            constants.ERROR_MSG_OF_INVALID_SIGNUP_LOGIN
        )


class SignUpWithNumericLoginTest(Test):
    INVALID_LOGIN = '1234'
    VALID_EMAIL = 'newemail@mail.ru'

    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = SignupForm(self.driver)
        signup_form.set_login(self.INVALID_LOGIN)
        signup_form.set_email(self.VALID_EMAIL)
        signup_form.set_password(os.environ['PASSWORD'])
        signup_form.set_confirm_password(os.environ['PASSWORD'])
        signup_form.submit()

        self.assertEqual(
            signup_form.get_login_error(),
            constants.ERROR_MSG_OF_INVALID_SIGNUP_LOGIN
        )


class SignUpWithLetterLoginTest(Test):
    INVALID_LOGIN = 'q'
    VALID_EMAIL = 'newemail@mail.ru'

    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = SignupForm(self.driver)
        signup_form.set_login(self.INVALID_LOGIN)
        signup_form.set_email(self.VALID_EMAIL)
        signup_form.set_password(os.environ['PASSWORD'])
        signup_form.set_confirm_password(os.environ['PASSWORD'])
        signup_form.submit()

        self.assertEqual(
            signup_form.get_login_error(),
            constants.ERROR_MSG_OF_INVALID_SIGNUP_LOGIN
        )


class SignUpWithInvalidEmailTest(Test):
    VALID_LOGIN = 'qwerrt123'
    INVALID_EMAIL = 'newem$$ail@mail.ru'

    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = SignupForm(self.driver)
        signup_form.set_login(self.VALID_LOGIN)
        signup_form.set_email(self.INVALID_EMAIL)
        signup_form.set_password(os.environ['PASSWORD'])
        signup_form.set_confirm_password(os.environ['PASSWORD'])
        signup_form.submit()

        self.assertEqual(
            signup_form.get_email_error(),
            constants.ERROR_MSG_OF_INVALID_SIGNUP_EMAIL
        )


class SignUpWithSmallPasswordTest(Test):
    VALID_LOGIN = 'qwerrt123'
    VALID_EMAIL = 'newemail@mail.ru'
    SMALL_PASSWORD = 'small'

    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = SignupForm(self.driver)
        signup_form.set_login(self.VALID_LOGIN)
        signup_form.set_email(self.VALID_EMAIL)
        signup_form.set_password(self.SMALL_PASSWORD)
        signup_form.set_confirm_password(self.SMALL_PASSWORD)
        signup_form.submit()

        self.assertEqual(
            signup_form.get_password_error(),
            constants.ERROR_MSG_OF_LEN_PASSWORD_SIGNUP
        )


class SignUpWithBigPasswordTest(Test):
    VALID_LOGIN = 'newlogin'
    VALID_EMAIL = 'newemail@mail.ru'
    BIG_PASSWORD = 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm'

    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = SignupForm(self.driver)
        signup_form.set_login(self.VALID_LOGIN)
        signup_form.set_email(self.VALID_EMAIL)
        signup_form.set_password(self.BIG_PASSWORD)
        signup_form.set_confirm_password(self.BIG_PASSWORD)
        signup_form.submit()

        self.assertEqual(
            signup_form.get_password_error(),
            constants.ERROR_MSG_OF_LEN_PASSWORD_SIGNUP
        )


class SignUpWithDifferentPasswordsTest(Test):
    VALID_LOGIN = 'newlogin'
    VALID_EMAIL = 'newemail@mail.ru'
    PASSWORD = 'qwerty123'
    CONFIRM_PASSWORD = 'qwerty1234'

    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = SignupForm(self.driver)
        signup_form.set_login(self.VALID_LOGIN)
        signup_form.set_email(self.VALID_EMAIL)
        signup_form.set_password(self.PASSWORD)
        signup_form.set_confirm_password(self.CONFIRM_PASSWORD)
        signup_form.submit()

        self.assertEqual(
            signup_form.get_confirm_password_error(),
            constants.ERROR_MSG_OF_DIFFERENT_PASSWORDS_SIGNUP
        )


class SignUpWithAllInvalidFieldsTest(Test):
    INVALID_LOGIN = 'newlogin@@'
    INVALID_EMAIL = 'newemai$$l@mail.ru'
    INVALID_PASSWORD = '1'
    CONFIRM_INVALID_PASSWORD = '2'

    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = SignupForm(self.driver)
        signup_form.set_login(self.INVALID_LOGIN)
        signup_form.set_email(self.INVALID_EMAIL)
        signup_form.set_password(self.INVALID_PASSWORD)
        signup_form.set_confirm_password(self.CONFIRM_INVALID_PASSWORD)
        signup_form.submit()

        self.assertEqual(
            signup_form.get_login_error(),
            constants.ERROR_MSG_OF_INVALID_SIGNUP_LOGIN
        )


class SignUpAlreadySignupedTest(Test):
    VALID_LOGIN = 'newlogin'

    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = SignupForm(self.driver)
        signup_form.set_login(self.VALID_LOGIN)
        signup_form.set_email(os.environ['LOGIN'])
        signup_form.set_password(os.environ['PASSWORD'])
        signup_form.set_confirm_password(os.environ['PASSWORD'])
        signup_form.submit()

        self.assertEqual(
            signup_page.BASE_URL + signup_page.PATH,
            self.driver.current_url
        )

