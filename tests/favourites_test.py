import constants
from pages.favourites import FavouritesPage
from pages.details import DetailsPage
from tests.default_authorized import TestAuthorized
from tests.default import Test


class NotOpenedTest(Test):
    def test(self):
        favourites_page = FavouritesPage(self.driver)
        favourites_page.open()

        self.assertFalse(favourites_page.is_has_favourites())


class ClickOnMovieTest(TestAuthorized):
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

        favourites_page.click_on_first_movie()

        self.assertEqual(
            id_of_movie,
            details_page.get_movie_id()
        )


class OnlyAddedMoviesTest(TestAuthorized):
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
        self.assertEqual(
            id_of_movie,
            favourites_page.get_id_of_last_fav_movie()
        )
