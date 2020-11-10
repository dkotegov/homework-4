from margarita import utils
from margarita.pages.virusmusic.main_page import MainPage
from margarita.tests.virusmusic.search.default import SearchTest


class SearchArtistOneResultTest(SearchTest):
    def test(self):
        page = MainPage(self.driver)
        page.open()

        page.enter_search("Black Ant")
        page.search_result("artist", "Black Ant")
        utils.wait_for_url(self.driver, "https://virusmusic.fun/artist/8")


class SearchAlbumOneResultTest(SearchTest):
    def test(self):
        page = MainPage(self.driver)
        page.open()

        page.enter_search("handmade")
        page.search_result("album", "#handmade")
        utils.wait_for_url(self.driver, "https://virusmusic.fun/album/8")


class SearchTrackOneResultTest(SearchTest):
    def test(self):
        page = MainPage(self.driver)
        page.open()

        page.enter_search("One And")
        page.search_result("track", "One And")
        page.get_current_id()

