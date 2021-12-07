from pages.main_page import MainPage
from tests.base import BaseTest


class MainPageTestSuite(BaseTest):
    def test_movie_page_transition(self):
        main = MainPage(self.driver)
        main.open()
        title = main.get_first_movie_card().get_attribute('data-tooltip')
        main.go_to_first_movie_page()
        self.assertEqual(main.get_movie_title(), title)


