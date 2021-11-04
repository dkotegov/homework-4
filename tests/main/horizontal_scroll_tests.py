from pages.main import MainPage
from tests.default import Test


class HorizontalScrollRightTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.click_right_scroll()
