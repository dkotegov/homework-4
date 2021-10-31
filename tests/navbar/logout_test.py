import constants
from pages.main import MainPage
from tests.default_authorized import TestAuthorized


class LogoutTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.click_on_logout()
        self.assertEqual(self.driver.current_url, constants.BASE_URL)
