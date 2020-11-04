import unittest
from selenium import webdriver

from pages.category_page import CategoryPage as page


class CategoryTests(unittest.TestCase):
    browser = webdriver.Chrome('./chromedriver')
    page = None

    @classmethod
    def setUpClass(cls):
        CategoryTests.page = page(CategoryTests.browser)
        CategoryTests.page.login()

    def test_select_category(self):
        self.page.open_main_page()
        self.page.click_category_button()
        category_chosen = self.page.select_category()
        page_main_category = self.page.get_main_category_text()
        page_border_category = self.page.get_border_category_text()
        self.assertEqual(category_chosen, page_main_category, page_border_category)

    def test_select_all_categories(self):
        self.page.open_main_page()
        self.page.click_category_button()
        self.page.select_all_categories()

    def test_select_gold_fond(self):
        self.page.open_main_page()
        self.page.click_category_button()
        self.page.select_gold_fond()

    @classmethod
    def tearDownClass(cls):
        CategoryTests.browser.quit()
