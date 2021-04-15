import unittest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from setup.default_setup import default_setup


class CheckSearch(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.main_page.open()
    
    def test_check_search_line_appearance(self):
        self.main_page.open_search_line()
        is_all_right = self.main_page.check_search_line_appearance()
        self.assertTrue(is_all_right)
    
    def test_check_search_line_disappearance_by_click(self):
        self.main_page.open_search_line()
        self.main_page.search_by_click()
        is_all_right = self.main_page.check_search_line_disappearance()
        self.assertTrue(is_all_right)
    
    def test_check_search_line_disappearance_by_Enter(self):
        self.main_page.open_search_line()
        self.main_page.search_by_Enter()
        is_all_right = self.main_page.check_search_line_disappearance()
        self.assertTrue(is_all_right)

    def test_check_search_prompt_window_appearance(self):
        self.main_page.input_text_into_search_line()
        is_all_right = self.main_page.check_search_prompt_window_appearance()
        self.assertTrue(is_all_right)

    def test_check_searching_by_click(self):
        self.main_page.input_text_into_search_line()
        self.main_page.search_by_click()
        is_all_right = self.search_page.check_appearance()
        self.assertTrue(is_all_right)
    
    def test_check_searching_by_Enter(self):
        self.main_page.input_text_into_search_line()
        self.main_page.search_by_Enter()
        is_all_right = self.search_page.check_appearance()
        self.assertTrue(is_all_right)
    
    def test_check_searching_by_prompt(self):
        self.main_page.input_text_into_search_line()
        self.main_page.choise_prompt()
        is_all_right = self.main_page.check_info_popup_appearance()
        self.assertTrue(is_all_right)

    def tearDown(self):
        self.driver.quit()
