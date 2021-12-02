from pages.movies import MoviesPage
from pages.genre import GenrePage
from pages.details import DetailsPage
from tests.default import Test
import constants


class ClickOnMovieGenreTest(Test):
    def test(self):
        movies_page = MoviesPage(self.driver)
        genre_page = GenrePage(self.driver)

        movies_page.open()
        genre_name = movies_page.get_name_of_first_genre()
        movies_page.click_on_first_genre()

        self.assertEqual(
            genre_name,
            genre_page.get_genre_name()
        )


class ClickOnMovieTest(Test):
    def test(self):
        movies_page = MoviesPage(self.driver)
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)

        movies_page.open()
        title = movies_page.get_title_of_first_movie()
        movies_page.click_on_first_movie()

        self.assertEqual(
            title,
            details_page.get_title()
        )
