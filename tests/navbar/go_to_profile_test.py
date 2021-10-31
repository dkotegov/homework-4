from pages.main import MainPage
from tests.default_authorized import TestAuthorized

from constants import BASE_URL


class GoToProfileTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.click_on_profile()
        self.assertEqual(self.driver.current_url, BASE_URL + 'profile')
