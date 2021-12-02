from pages.series import SeriesPage
from pages.genre import GenrePage
from tests.default import Test
from pages.details import DetailsPage
import constants


class ClickOnGenreTest(Test):
    def test(self):
        series_page = SeriesPage(self.driver)
        genre_page = GenrePage(self.driver)

        series_page.open()
        genre_name = series_page.get_name_of_first_genre()
        series_page.click_on_first_genre()

        self.assertEqual(
            genre_name,
            genre_page.get_genre_name()
        )


class ClickOnSeriesTest(Test):
    def test(self):
        series_page = SeriesPage(self.driver)
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)

        series_page.open()
        title = series_page.get_title_of_first_movie()
        series_page.click_on_first_movie()

        self.assertEqual(
            title,
            details_page.get_title()
        )
