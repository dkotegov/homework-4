import os

from pages.login import LoginPage
from pages.main import MainPage
from pages.profile import ProfilePage
from components.profile_form import ProfileForm

from tests.default import Test
import constants


class InvalidEmailLoginTest(Test):
    def test(self):
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.click_login()

        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.auth_with(constants.INVALID_EMAIL, constants.WRONG_PASSWORD)

        self.assertTrue(auth_page.has_email_error())


class EmptyFieldsLoginTest(Test):
    def test(self):
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.click_login()

        self.assertTrue(auth_page.has_email_error())
        self.assertTrue(auth_page.has_password_error())


class GoToSignupTest(Test):
    def test(self):
        auth_page = LoginPage(self.driver)
        auth_page.open()

        auth_page.click_on_register()

        self.assertEqual(
            self.driver.current_url,
            auth_page.BASE_URL + 'signup'
        )


class LoginTest(Test):
    def test(self):
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.auth()

        main_page = MainPage(self.driver)
        main_page.wait_for_container()

        profile_page = ProfilePage(self.driver)
        profile_page.open()
        profile_form = ProfileForm(self.driver)

        self.assertEqual(
            os.environ['LOGIN'],
            profile_form.get_email()
        )


class WrongCredsLoginTest(Test):
    def test(self):
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.click_login()

        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.auth_with('invalid@invalid.com', 'invalid_password')

        self.assertTrue(auth_page.has_email_error())
        self.assertTrue(auth_page.has_password_error())


class WrongPasswordLoginTest(Test):
    def test(self):
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.click_login()

        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.auth_with(os.environ['LOGIN'], 'invalid_password')

        self.assertTrue(auth_page.has_email_error())
        self.assertTrue(auth_page.has_password_error())
