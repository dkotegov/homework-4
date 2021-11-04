import constants
from pages.favourites import FavouritesPage
from pages.details import DetailsPage
from tests.default_authorized import TestAuthorized


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
        
        favourites_page = FavouritesPage(self.driver)
        favourites_page.open()
        
        id_of_movie = details_page.get_movie_id()
        favourites_page.click_on_first_movie()

        self.assertEqual(
            id_of_movie,
            details_page.get_movie_id()
        )
