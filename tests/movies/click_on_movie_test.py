import constants
from pages.movies import MoviesPage
from pages.details import DetailsPage
from tests.default import Test


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
