from random import randrange

from pages.signup_page import SignupPage
from pages.auth_page import AuthPage
from pages.main_page import MainPage

from tests.base_test import BaseTest


class SignupTest(BaseTest):
    GOOD_USERNAME_TEMPLATE = 'testUserForSignupTests{}'
    BAD_USERNAME = 'wo-+[]123412342[][][][][][] ][ ][ !!!@'

    GOOD_PASSWORD = 'ASDasfc34c3fzDScadsf3w'
    BAD_PASSWORD = 'qw12'

    GOOD_EMAIL = 'wolf@liokor.ru'
    BAD_EMAIL = 'wo@'

    def setUp(self) -> None:
        self.page = SignupPage(self.driver)
        self.page.open()

    def tearDown(self) -> None:
        self.driver.delete_all_cookies()

    def _generate_random_username(self):
        return self.GOOD_USERNAME_TEMPLATE.format(randrange(0, 4000000000))

    def test_empty_username(self):
        self.page.set_username('')
        self.page.set_password(self.GOOD_PASSWORD)
        self.page.set_password_confirm(self.GOOD_PASSWORD)
        self.page.click_signup_btn()

        err = self.page.get_username_error()
        self.assertNotEqual(len(err), 0)

    def test_bad_username(self):
        self.page.set_username(self.BAD_USERNAME)
        self.page.set_password(self.GOOD_PASSWORD)
        self.page.set_password_confirm(self.GOOD_PASSWORD)
        self.page.click_signup_btn()

        err = self.page.get_username_error()
        self.assertNotEqual(len(err), 0)

    def test_empty_password(self):
        self.page.set_username(self._generate_random_username())
        self.page.set_password('')
        self.page.set_password_confirm(self.GOOD_PASSWORD)
        self.page.click_signup_btn()

        err = self.page.get_password_error()
        self.assertNotEqual(len(err), 0)

    def test_bad_password(self):
        self.page.set_username(self._generate_random_username())
        self.page.set_password(self.BAD_PASSWORD)
        self.page.set_password_confirm(self.BAD_PASSWORD)
        self.page.click_signup_btn()

        err = self.page.get_password_error()
        self.assertNotEqual(len(err), 0)

    def test_bad_email(self):
        self.page.set_username(self._generate_random_username())
        self.page.set_password(self.GOOD_PASSWORD)
        self.page.set_password_confirm(self.GOOD_PASSWORD)
        self.page.set_email(self.BAD_EMAIL)
        self.page.click_signup_btn()

        err = self.page.get_email_error()
        self.assertNotEqual(len(err), 0)

    def test_success_signup(self):
        username = self._generate_random_username()

        self.page.set_username(username)
        self.page.set_password(self.GOOD_PASSWORD)
        self.page.set_password_confirm(self.GOOD_PASSWORD)
        self.page.set_email(self.GOOD_EMAIL)
        self.page.click_signup_btn()

        main_page = MainPage(self.driver)
        self.assertEqual(main_page.is_opened(), True)

        email = main_page.get_authenticated_user_email()
        actual_username = email.split('@')[0]
        self.assertEqual(actual_username.lower(), username.lower())

    def test_auth_btn(self):
        self.page.click_auth_btn()

        self.assertEqual(AuthPage(self.driver).is_opened(), True)
