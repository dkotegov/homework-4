import os

from pages.signup import SignupPage
from pages.profile import ProfilePage
from pages.main import MainPage
from components.signup_form import SignupForm
from components.profile_form import ProfileForm
from tests.default import Test


class SignUpTest(Test):
    VALID_LOGIN = 'newlogin'
    VALID_EMAIL = 'testqa2@mail.ru'

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

