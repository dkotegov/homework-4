import utils
from pages.movies import MoviesPage
from tests.default_authorized import TestAuthorized
from components.navbar import NavBar

from constants import BASE_URL


class GoToMainTest(TestAuthorized):
    def test(self):
        movies_page = MoviesPage(self.driver)
        movies_page.open()
        movies_page.set_navbar()
        movies_page.navbar.click_on_main()
        self.assertEqual(self.driver.current_url, BASE_URL)
