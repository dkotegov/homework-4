from margarita.pages.virusmusic.main_page import MainPage
from margarita.pages.virusmusic.profile import ProfilePlaylistsPage
from margarita.tests.virusmusic.tracks.default import TrackTestAuth
from nikita.pages.virusmusic.playlist import PlaylistPage


class TrackAddAndRemoveFromPlaylistTest(TrackTestAuth):
    def test(self):
        profile = ProfilePlaylistsPage(self.driver)
        profile.create_playlist("QA")
        playlist_id = profile.get_playlist_id("QA")

        main = MainPage(self.driver)
        main.open()

        track_id = main.get_first_track_id()
        is_added_before = main.press_add_to_playlist(track_id, "QA", playlist_id)
        is_added_after = main.press_add_to_playlist(track_id, "QA", playlist_id)
        playlist = PlaylistPage(self.driver, playlist_id)
        playlist.delete()
        self.assertNotEqual(is_added_before, is_added_after)
