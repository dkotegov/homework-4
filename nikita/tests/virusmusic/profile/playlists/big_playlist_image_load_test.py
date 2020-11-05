import os

from nikita.tests.virusmusic.profile.playlists.default import PlaylistTest
from nikita.pages.virusmusic.profile.playlists import ProfilePlaylistsPage
from nikita.utils import wait_for_pop_up
from nikita.constants import PLAYLIST_NAME

class BigPlaylistImageLoadTest(PlaylistTest):
    BIG_IMAGE_PATH = os.getcwd() + '/nikita/resources/iiL9jsEie_w.jpg'

    def test(self):
        page = ProfilePlaylistsPage(self.driver)
        page.load_image(PLAYLIST_NAME, self.BIG_IMAGE_PATH)
        wait_for_pop_up(self.driver, success=False)
