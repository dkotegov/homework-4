import unittest

from pages.content_page import ContentPage
from setup.default_setup import default_setup


class CheckContent(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.content_page = ContentPage(self.driver)
        self.content_page.open()
    
    def test_check_filters_appearance(self):
        self.content_page.open_filters()
        is_all_right = self.content_page.check_filters_appearance()
        self.assertTrue(is_all_right)

    def test_check_selecting_filters(self):
        self.content_page.select_genre_filter()
        is_all_right = self.content_page.check_selected_filters()
        self.assertTrue(is_all_right)
    
    def test_check_clearing_filters(self):
        self.content_page.select_filters()
        self.content_page.clear_all()
        is_all_right = self.content_page.check_filters_all_clear()
        self.assertTrue(is_all_right)

    def tearDown(self):
        self.driver.quit()
