from pages.series import SeriesPage
from pages.details import DetailsPage
from tests.default import Test


class ClickOnSeriesTest(Test):
    def test(self):
        series_page = SeriesPage(self.driver)
        details_page = DetailsPage(self.driver)

        series_page.open()
        title = series_page.get_title_of_first_movie()
        series_page.click_on_first_movie()

        self.assertEqual(
            title,
            details_page.get_title()
        )
