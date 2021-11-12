from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.signup_page import SignupPage

from tests.base_test import BaseTest

import settings as s


class AuthTest(BaseTest):
    def setUp(self) -> None:
        self.page = AuthPage(self.driver)
        self.page.open()

    def tearDown(self) -> None:
        self.driver.delete_all_cookies()

    def test_auth(self):
        self.page.auth()

        main_page = MainPage(self.driver)
        auth_email = main_page.get_authenticated_user_email()

        actual_username = auth_email.split('@')[0].lower()
        expected_username = s.USERNAME.lower()

        self.assertEqual(actual_username, expected_username)

    def test_username_empty_error(self):
        self.page.set_username('')
        self.page.set_password()
        self.page.click_login_btn()
        err = self.page.get_username_error()

        self.assertNotEqual(len(err), 0)

    def test_password_empty_error(self):
        self.page.set_username()
        self.page.set_password('')
        self.page.click_login_btn()
        err = self.page.get_password_error()

        self.assertNotEqual(len(err), 0)

    def test_incorrect_username_error(self):
        self.page.set_username(s.USERNAME + '[]!@%$___---1342')
        self.page.set_password(s.PASSWORD)
        self.page.click_login_btn()

        username_error = self.page.get_username_error()
        password_error = self.page.get_password_error()

        self.assertNotEqual(len(username_error), 0)
        self.assertNotEqual(len(password_error), 0)

    def test_incorrect_password_error(self):
        self.page.set_username(s.USERNAME)
        self.page.set_password(s.PASSWORD + 'wolf')
        self.page.click_login_btn()

        username_error = self.page.get_username_error()
        password_error = self.page.get_password_error()

        self.assertNotEqual(len(username_error), 0)
        self.assertNotEqual(len(password_error), 0)

    def test_signup_btn(self):
        self.page.click_signup_btn()

        self.assertTrue(SignupPage(self.driver).is_opened())
