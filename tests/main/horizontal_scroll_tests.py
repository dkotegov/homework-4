from pages.main import MainPage
from tests.default import Test


class HorizontalScrollRightTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.click_right_scroll_until_visible()
        self.assertFalse(main_page.is_right_scroll_visible())


class HorizontalScrollLeftTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.click_right_scroll_until_visible()
        main_page.click_left_scroll_until_visible()
        self.assertFalse(main_page.is_left_scroll_visible())
