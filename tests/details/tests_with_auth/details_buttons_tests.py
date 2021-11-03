import os

from selenium.webdriver import DesiredCapabilities, Remote

from pages.details import DetailsPage
from pages.favourites import FavouritesPage
from tests.default_authorized import TestAuthorized

import constants
from pages.login import LoginPage


class OpenPlayerTest(TestAuthorized):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()

        details_page.open_player()

        self.assertTrue(details_page.is_player_opened())


class AddToFavouritesTest(TestAuthorized):
    def tearDown(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()
        details_page.remove_from_favourite()
        details_page.open_player()
        self.driver.quit()

    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()

        details_page.add_to_favourites()
        id_of_movie = details_page.get_movie_id()

        favourites_page = FavouritesPage(self.driver)
        favourites_page.open()

        self.assertEqual(
            id_of_movie,
            favourites_page.get_id_of_first_fav_movie()
        )


class RemoveFromFavouritesTest(TestAuthorized):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.auth()

        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()
        details_page.add_to_favourites()

    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()

        details_page.remove_from_favourite()

        favourites_page = FavouritesPage(self.driver)
        favourites_page.open()

        self.assertFalse(favourites_page.is_has_favourites())


class LikeMovieTest(TestAuthorized):
    is_liked = False
    is_disliked = False

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.auth()

        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()
        self.is_liked = details_page.is_liked()
        self.is_disliked = details_page.is_disliked()
        if self.is_liked:
            details_page.dislike()
            details_page.wait_for_disliked()

    def tearDown(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()
        if self.is_disliked:
            details_page.dislike()
            details_page.wait_for_disliked()
        self.driver.quit()

    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()

        details_page.like()
        details_page.wait_for_liked()
        old_rating = details_page.get_rating()
        details_page.open()

        self.assertNotEqual(
            old_rating,
            details_page.get_rating()
        )


class DisikeMovieTest(TestAuthorized):
    is_liked = False
    is_disliked = False

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_page.auth()

        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()
        self.is_liked = details_page.is_liked()
        self.is_disliked = details_page.is_disliked()
        if self.is_disliked:
            details_page.like()
            details_page.wait_for_liked()

    def tearDown(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()
        if self.is_liked:
            details_page.like()
            details_page.wait_for_liked()
        self.driver.quit()

    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()

        details_page.dislike()
        details_page.wait_for_disliked()
        old_rating = details_page.get_rating()
        details_page.open()

        self.assertNotEqual(
            old_rating,
            details_page.get_rating()
        )
