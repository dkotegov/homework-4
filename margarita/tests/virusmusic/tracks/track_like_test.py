from margarita.tests.virusmusic.tracks.default import TrackTestAuth
from margarita.tests.virusmusic.tracks.default import TrackTestNoAuth
from margarita.pages.virusmusic.main_page import MainPage


class TrackLikeTest(TrackTestAuth):
    def test(self):
        page = MainPage(self.driver)
        page.open()
        track_id = page.get_first_track_id()

        is_liked_before = page.is_liked(track_id)
        page.press_track_like_button(track_id)
        is_liked_after = page.is_liked(track_id)

        self.assertNotEqual(is_liked_before, is_liked_after)


# site has a bug
class TrackLikeTestNoAuth(TrackTestNoAuth):
    def test(self):
        page = MainPage(self.driver)
        page.open()
        track_id = page.get_first_track_id()

        self.assertFalse(page.is_like_visible(track_id))
