from pages.signup import SignupPage
from pages.login import LoginPage

import constants

from tests.default import Test


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
