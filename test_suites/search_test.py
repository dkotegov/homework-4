import unittest

from pages.search_page import SearchPage as page


class SearchTests(unittest.TestCase):

    def test_asetup(self):
        self.page = page()
        self.page.login()

    def test_nav_search_input(self):
        self.page = page()
        self.page.test_nav_search_input("TEXT")

    def test_empty_query(self):
        self.page = page()
        self.page.test_empty_query("TEXT")

    def test_special_query(self):
        self.page = page()
        self.page.test_special_symb("TEXT")

    def test_only_quest_filter(self):
        self.page = page()
        self.page.test_question_only_button("TEXT")
