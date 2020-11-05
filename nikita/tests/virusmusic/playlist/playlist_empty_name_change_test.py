from nikita.tests.virusmusic.playlist.default import PlaylistTest
from nikita.pages.virusmusic.playlist import PlaylistPage
from nikita.utils import wait_for_pop_up

class PlaylistEmptyNameChangeTest(PlaylistTest):
    def test(self):
        page = PlaylistPage(self.driver, self.playlistId)
        page.change_name('')
        wait_for_pop_up(self.driver, success=False)
