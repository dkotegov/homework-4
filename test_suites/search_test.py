import unittest

from pages.search_page import SearchPage as page


class SearchTests(unittest.TestCase):
    TEST_TEXT = "TEXT"
    EMPTY_TEXT = ""
    SYMB_TEXT = "!@#$%^&*()"

    def test_a_setup(self):
        self.page = page()
        self.page.login()

    def test_nav_search_input(self):
        self.page = page()
        self.page.open_otvet_page()
        self.page.input_in_nav_search(self.TEST_TEXT)
        self.page.submit_nav_search()
        self.page.compare_search_text()

    def test_empty_query(self):
        self.page = page()
        self.page.open_otvet_page()
        self.page.input_in_nav_search(self.EMPTY_TEXT)
        self.page.submit_nav_search()
        self.page.check_empty_text()

    def test_special_query(self):
        self.page = page()
        self.page = page()
        self.page.open_otvet_page()
        self.page.input_in_nav_search(self.SYMB_TEXT)
        self.page.submit_nav_search()
        self.page.check_empty_res()

    def test_only_quest_filter(self):
        self.page = page()
        self.page.open_search_page()
        self.page.input_in_main_search(self.TEST_TEXT)
        self.page.submit_main_search()
        self.page.compare_counts()
