import unittest

from pages.category_page import CategoryPage as page


class CategoryTests(unittest.TestCase):

    def test_a_setup(self):
        self.page = page()
        self.page.login()


    def test_select_category(self):
        self.page = page()
        self.page.open_main_page()
        self.page.click_category_button()
        self.page.compare_categories()

    def test_select_all_categories(self):
        self.page = page()
        self.page.open_main_page()
        self.page.click_category_button()
        self.page.select_all_categories()

    def test_select_gold_fond(self):
        self.page = page()
        self.page.open_main_page()
        self.page.click_category_button()
        self.page.select_gold_fond()
