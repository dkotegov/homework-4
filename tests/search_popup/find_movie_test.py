import constants
from tests.default import Test
from components.search_popup import SearchPopup
from pages.main import MainPage
from pages.details import DetailsPage


class FindMovieTest(Test):
    MOVIE_TITLE = 'Гнев человеческий'

    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        search_popup = SearchPopup(self.driver)
        search_popup.open()
        search_popup.search(self.MOVIE_TITLE)
        search_popup.click_on_founded_item()

        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)

        self.assertEqual(
            self.MOVIE_TITLE,
            details_page.get_title()
        )
