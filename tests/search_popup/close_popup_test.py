from tests.default import Test
from components.search_popup import SearchPopup
from pages.main import MainPage


class ClosePopupTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        search_popup = SearchPopup(self.driver)
        search_popup.open()
        search_popup.close()

        self.assertFalse(search_popup.is_visible())
