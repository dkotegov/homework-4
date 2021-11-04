from tests.default import Test
from components.search_popup import SearchPopup
from pages.main import MainPage


class EnterLetterTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        search_popup = SearchPopup(self.driver)
        search_popup.open()
        search_popup.search('г')
        count_founded_items = search_popup.count_found_items()
        search_popup.search('гн')

        self.assertNotEqual(
            count_founded_items,
            search_popup.count_found_items()
        )
