from pages.details import DetailsPage
from tests.default import Test
import constants


class NotOpenedTest(Test):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()

        details_page.open_player()

        self.assertEqual(
            False,
            details_page.is_player_opened()
        )