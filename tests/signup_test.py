import os

from pages.signup import SignupPage
from pages.profile import ProfilePage
from pages.main import MainPage
from pages.login import LoginPage
from components.signup_form import SignupForm
from components.profile_form import ProfileForm
from tests.default import Test
import constants


class SignUpTest(Test):
    VALID_LOGIN = constants.VALID_SIGNUP_LOGIN
    VALID_EMAIL = constants.VALID_SIGNUP_EMAIL

    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = SignupForm(self.driver)
        signup_form.set_login(self.VALID_LOGIN)
        signup_form.set_email(self.VALID_EMAIL)
        signup_form.set_password(os.environ['PASSWORD'])
        signup_form.set_confirm_password(os.environ['PASSWORD'])
        signup_form.submit()

        main_page = MainPage(self.driver)
        main_page.wait_for_container()

        profile_page = ProfilePage(self.driver)
        profile_form = ProfileForm(self.driver)
        profile_page.open()

        self.assertEqual(
            self.VALID_EMAIL,
            profile_form.get_email()
        )

        self.assertEqual(
            self.VALID_LOGIN,
            profile_form.get_login()
        )


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
    INVALID_LOGIN = constants.INVALID_CYRILIC_SIGNUP_LOGIN
    VALID_EMAIL = constants.VALID_SIGNUP_EMAIL

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
    INVALID_LOGIN = constants.INVALID_NUMERIC_SIGNUP_LOGIN
    VALID_EMAIL = constants.VALID_SIGNUP_EMAIL

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
    INVALID_LOGIN = constants.INVALID_LETTER_SIGNUP_LOGIN
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
    VALID_LOGIN = constants.VALID_SIGNUP_LOGIN
    INVALID_EMAIL = constants.INVALID_SIGNUP_EMAIL

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
    VALID_LOGIN = constants.VALID_SIGNUP_LOGIN
    VALID_EMAIL = constants.VALID_SIGNUP_EMAIL
    SMALL_PASSWORD = constants.SMALL_SIGNUP_PASSWORD

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
    VALID_LOGIN = constants.VALID_SIGNUP_LOGIN
    VALID_EMAIL = constants.VALID_SIGNUP_EMAIL
    BIG_PASSWORD = constants.BIG_SIGNUP_PASSWORD

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
    VALID_LOGIN = constants.VALID_SIGNUP_LOGIN
    VALID_EMAIL = constants.VALID_SIGNUP_EMAIL
    PASSWORD = constants.SIGNUP_PASSWORD
    CONFIRM_PASSWORD = constants.SIGNUP_CONFIRM_PASSWORD

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
    INVALID_LOGIN = constants.INVALID_SIGNUP_LOGIN
    INVALID_EMAIL = constants.INVALID_SIGNUP_EMAIL
    INVALID_PASSWORD = constants.INVALID_SIGNUP_PASSWORD
    CONFIRM_INVALID_PASSWORD = constants.CONFIRM_INVALID_SIGNUP_PASSWORD

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
    VALID_LOGIN = constants.VALID_SIGNUP_LOGIN

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


class TransitToLoginPageTest(Test):
    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_page.click_on_login_page_link()

        login_page = LoginPage(self.driver)
        title_of_page = login_page.get_title_of_page()

        self.assertEqual(
            title_of_page,
            constants.TITLE_OF_LOGIN_PAGE
        )
