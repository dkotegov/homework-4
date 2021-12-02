import os

from selenium.webdriver import DesiredCapabilities, Remote

from pages.details import DetailsPage
from pages.favourites import FavouritesPage
from pages.profile import ProfilePage
from pages.actor import ActorPage
from tests.default_authorized import TestAuthorized
from tests.default import Test

import constants
from pages.login import LoginPage


class ClickOnActorNameTest(Test):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()

        actor_name = details_page.get_name_of_last_actor()
        details_page.click_on_last_actor()

        actor_page = ActorPage(self.driver, constants.ID_OF_ACTOR)

        self.assertEqual(
            actor_name,
            actor_page.get_name_of_actor()
        )


class TransitToAuthTest(Test):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()

        details_page.transit_by_stub()

        login_page = LoginPage(self.driver)
        title_of_page = login_page.get_title_of_page()

        self.assertEqual(
            title_of_page,
            constants.TITLE_OF_LOGIN_PAGE
        )


class OpenPlayerTest(TestAuthorized):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()

        details_page.open_player()

        self.assertTrue(details_page.is_player_opened())


class TransitToProfileTest(TestAuthorized):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_PAID_MOVIE)
        details_page.open()

        details_page.transit_by_stub()

        profile_page = ProfilePage(self.driver)
        title_of_page = profile_page.get_title_of_page()

        self.assertEqual(
            title_of_page,
            constants.TITLE_OF_PROFILE_PAGE
        )


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
        super().setUp()

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


class DislikeMovieTest(TestAuthorized):
    is_liked = False
    is_disliked = False

    def setUp(self):
        super().setUp()

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
