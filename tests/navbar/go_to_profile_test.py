from pages.main import MainPage
from tests.default_authorized import TestAuthorized

from utils import wait_for_url


class GoToProfileTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.click_on_profile()
