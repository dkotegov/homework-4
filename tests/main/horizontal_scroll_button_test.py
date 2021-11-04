from pages.main import MainPage
from tests.default import Test


class HorizontalScrollTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        visible_cards = main_page.get_visible_card_titles()
        main_page.click_scroll_button()
        new_visible_cards = main_page.get_visible_card_titles()
        self.assertNotEqual(visible_cards, new_visible_cards)
