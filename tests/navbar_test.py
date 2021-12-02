import utils
from pages.main import MainPage
from pages.movies import MoviesPage
from tests.default_authorized import TestAuthorized

from constants import BASE_URL


class GoToFavouritesTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.set_navbar()
        main_page.navbar.click_on_favourites()
        self.assertEqual(self.driver.current_url, BASE_URL + 'favourite')


class LogoutTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.set_navbar()
        main_page.navbar.click_on_logout()
        main_page.open()
        self.assertTrue(main_page.navbar.is_visible_login())


class GoToSeriesTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.set_navbar()
        main_page.navbar.click_on_series()
        self.assertEqual(self.driver.current_url, BASE_URL + 'series')


class GoToProfileTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.set_navbar()
        main_page.navbar.click_on_profile()
        self.assertEqual(self.driver.current_url, BASE_URL + 'profile')


class GoToMoviesTest(TestAuthorized):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.set_navbar()
        main_page.navbar.click_on_series()
        self.assertEqual(self.driver.current_url, BASE_URL + 'series')


class GoToMainTest(TestAuthorized):
    def test(self):
        movies_page = MoviesPage(self.driver)
        movies_page.open()
        movies_page.set_navbar()
        movies_page.navbar.click_on_main()
        self.assertEqual(self.driver.current_url, BASE_URL)
