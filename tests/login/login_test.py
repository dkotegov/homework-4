import os

from pages.login import LoginPage
from pages.main import MainPage
from pages.profile import ProfilePage
from components.profile_form import ProfileForm

from tests.default import Test


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
