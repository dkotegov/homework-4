from pages.details import DetailsPage
from tests.default_authorized import TestAuthorized
import constants


class ClosedTest(TestAuthorized):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()
        details_page.set_player()

        details_page.open_player()
        details_page.player.click_on_close()

        self.assertEqual(
            False,
            details_page.is_player_opened()
        )