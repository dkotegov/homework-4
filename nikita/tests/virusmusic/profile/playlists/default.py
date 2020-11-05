from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.playlists import ProfilePlaylistsPage
from nikita.utils import wait_for_pop_up
from nikita.constants import PLAYLIST_NAME

class PlaylistTest(Test):
    def setUp(self):
        super().setUp()
        page = ProfilePlaylistsPage(self.driver)
        page.create_playlist(PLAYLIST_NAME)
        wait_for_pop_up(self.driver)
        page.wait_for_playlist(PLAYLIST_NAME)

    def tearDown(self):
        page = ProfilePlaylistsPage(self.driver)
        page.delete_playlist(PLAYLIST_NAME)
        super().tearDown()
