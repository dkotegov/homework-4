from nikita.tests.virusmusic.profile.playlists.default import PlaylistTest
from nikita.pages.virusmusic.profile.playlists import ProfilePlaylistsPage
from nikita.utils import wait_for_pop_up
from nikita.constants import PLAYLIST_NAME

class PlaylistNameChangeTest(PlaylistTest):
    NEW_PLAYLIST_NAME = 'kek'

    def test(self):
        page = ProfilePlaylistsPage(self.driver)
        page.change_name(PLAYLIST_NAME, self.NEW_PLAYLIST_NAME)
        wait_for_pop_up(self.driver)
