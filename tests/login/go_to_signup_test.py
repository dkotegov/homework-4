from pages.login import LoginPage

from tests.default import Test


class GoToSignupTest(Test):
    def test(self):
        auth_page = LoginPage(self.driver)
        auth_page.open()

        auth_page.click_on_register()

        self.assertEqual(
            self.driver.current_url,
            auth_page.BASE_URL + 'signup'
        )
