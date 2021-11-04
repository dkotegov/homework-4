import utils
from pages.main import MainPage
from tests.default_authorized import TestAuthorized

from constants import BASE_URL


class GoToMoviesTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.set_navbar()
        main_page.navbar.click_on_series()
        self.assertEqual(self.driver.current_url, BASE_URL + 'series')
