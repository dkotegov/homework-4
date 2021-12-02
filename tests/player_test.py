from pages.details import DetailsPage
from tests.default_authorized import TestAuthorized
from tests.default import Test
import constants


# bug
class CloseFullscreenTest(TestAuthorized):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()
        details_page.set_player()

        details_page.open_player()
        details_page.player.click_on_fullscreen()
        details_page.player.click_on_partscreen()
        details_page.player.wait_for_fullscreen_btn()

        self.assertFalse(details_page.player.is_fullscreen())


class NotOpenedTest(Test):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()


# bug
class EscToPartScreenTest(TestAuthorized):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()
        details_page.set_player()

        details_page.open_player()
        details_page.player.click_on_fullscreen()
        details_page.player.esc_to_part_screen()
        details_page.player.wait_for_fullscreen_btn()

        self.assertFalse(details_page.player.is_fullscreen())
        self.assertFalse(details_page.could_open_player())


class ClosedTest(TestAuthorized):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()
        details_page.set_player()

        details_page.open_player()
        details_page.player.click_on_close()

        self.assertFalse(details_page.is_player_opened())
