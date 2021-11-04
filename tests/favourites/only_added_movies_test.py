from pages.details import DetailsPage
from pages.favourites import FavouritesPage
from tests.default_authorized import TestAuthorized

import constants

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