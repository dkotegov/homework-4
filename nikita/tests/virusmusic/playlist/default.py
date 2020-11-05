from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.playlists import ProfilePlaylistsPage
from nikita.pages.virusmusic.playlist import PlaylistPage
from nikita.utils import wait_for_pop_up, wait_for_url
from nikita.constants import VIRUSMUSIC_BASE_URL, PLAYLIST_NAME

class PlaylistTest(Test):
    def setUp(self):
        super().setUp()
        page = ProfilePlaylistsPage(self.driver)
        page.create_playlist(PLAYLIST_NAME)
        wait_for_pop_up(self.driver)
        page.wait_for_playlist(PLAYLIST_NAME)
        self.playlistId = page.get_playlist_id(PLAYLIST_NAME)

    def tearDown(self):
        page = PlaylistPage(self.driver, self.playlistId)
        page.delete()
        wait_for_pop_up(self.driver)
        wait_for_url(self.driver, VIRUSMUSIC_BASE_URL + 'profile/playlists')
        super().tearDown()
