from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.playlists import ProfilePlaylistsPage
from nikita.utils import wait_for_pop_up

class PlaylistWithEmptyNameCreationTest(Test):
    def test(self):
        page = ProfilePlaylistsPage(self.driver)
        page.create_playlist('')
        wait_for_pop_up(self.driver, success=False)
