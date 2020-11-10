from margarita.pages.virusmusic.main_page import MainPage
from margarita.tests.virusmusic.search.default import SearchTest


class SearchNoResults(SearchTest):
    def test(self):
        page = MainPage(self.driver)
        page.open()

        page.enter_search("ыыыыыыыыы")
        page.wait_for_not_found_search()
