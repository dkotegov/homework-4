import clipboard

from nikita.tests.virusmusic.playlist.default import PlaylistTest
from nikita.pages.virusmusic.playlist import PlaylistPage

class PlaylistCopyLinkTest(PlaylistTest):
    def test(self):
        page = PlaylistPage(self.driver, self.playlistId)
        page.copy_link()
        self.assertEqual(
            clipboard.paste(),
            self.driver.current_url
        )
