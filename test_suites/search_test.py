import unittest

from pages.search_page import SearchPage as page


class SearchTests(unittest.TestCase):

    def test_nav_search_input(self):
        self.page = page()
        self.page.login()
        self.page.test_nav_search_input()
