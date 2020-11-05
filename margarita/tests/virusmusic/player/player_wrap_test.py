from time import sleep

from margarita.tests.virusmusic.player.default import Test
from margarita.pages.virusmusic.main_page import MainPage


class TestWrapPlayer(Test):
    def test(self):
        page = MainPage(self.driver)
        page.open()
        track_id = page.get_first_track_id()
        page.play(track_id)
        # time for player to move
        sleep(1)
        player_pos_before = page.get_player_pos()
        page.wrap_player()
        player_pos_after = page.get_player_pos()

        self.assertNotEqual(player_pos_after, player_pos_before)
