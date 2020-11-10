
from margarita import utils
from margarita.pages.virusmusic.main_page import MainPage
from margarita.tests.virusmusic.search.default import SearchTest


class SearchArtistTest(SearchTest):
    def test(self):
        page = MainPage(self.driver)
        page.open()

        page.enter_search("An")
        page.search_result("artist", "Black Ant")
        utils.wait_for_url(self.driver, "https://virusmusic.fun/artist/8")


class SearchAlbumTest(SearchTest):
    def test(self):
        page = MainPage(self.driver)
        page.open()

        page.enter_search("An")
        page.search_result("album", "#handmade")
        utils.wait_for_url(self.driver, "https://virusmusic.fun/album/8")


class SearchTrackTest(SearchTest):
    def test(self):
        page = MainPage(self.driver)
        page.open()

        page.enter_search("An")
        page.search_result("track", "One And")
        page.get_current_id()


class SearchAllResults(SearchTest):
    def test(self):
        page = MainPage(self.driver)
        page.open()

        page.enter_search("An")
        page.press_search_button()

        utils.wait_for_url(self.driver, "https://virusmusic.fun/search/An")
