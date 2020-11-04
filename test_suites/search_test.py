import unittest
from selenium import webdriver

from pages.search_page import SearchPage as page


class SearchTests(unittest.TestCase):
    TEST_TEXT = "TEXT"
    EMPTY_QUERY = ""
    SYMB_TEXT = "!@#$%^&*()"

    EMPTY_TEXT = "Задан пустой\nпоисковый запрос"
    EMPTY_RES = "По вашему запросу\nничего не найдено"

    browser = webdriver.Chrome('./chromedriver')
    page = None

    @classmethod
    def setUpClass(cls):
        SearchTests.page = page(SearchTests.browser)
        SearchTests.page.login()

    def test_nav_search_input(self):
        self.page.open_otvet_page()
        self.page.input_in_nav_search(self.TEST_TEXT)
        self.page.submit_nav_search()
        self.assertEqual(self.page.get_main_search_text(), self.page.get_nav_search_text())

    def test_empty_query(self):
        self.page.open_otvet_page()
        self.page.input_in_nav_search(self.EMPTY_QUERY)
        self.page.submit_nav_search()
        empty_text = self.page.check_empty_text()
        self.assertEqual(empty_text, self.EMPTY_TEXT)

    def test_special_query(self):
        self.page.open_otvet_page()
        self.page.input_in_nav_search(self.SYMB_TEXT)
        self.page.submit_nav_search()
        empty_res = self.page.check_empty_res()
        self.assertEqual(empty_res, self.EMPTY_RES)

    def test_long_search_query(self):
        self.page.open_search_page()
        self.page.input_in_main_search(self.TEST_TEXT * round(750 / (len(self.TEST_TEXT))))
        self.page.submit_main_search()
        empty_res = self.page.check_empty_res()
        self.assertEqual(empty_res, self.EMPTY_RES)

    def test_only_quest_filter(self):
        self.page.open_search_page()
        self.page.input_in_main_search(self.TEST_TEXT)
        self.page.submit_main_search()
        total_count = self.page.get_total_count()
        self.page.toggle_only_question_checkbox()
        self.page.submit_main_search()
        only_question_count = self.page.get_total_count()
        self.assertGreaterEqual(total_count, only_question_count)

    def test_category_change(self):
        self.page.open_search_page()
        self.page.input_in_main_search(self.TEST_TEXT)
        self.page.submit_main_search()

        total_count = self.page.get_total_count()
        self.page.click_select_category()
        self.page.select_category()
        self.page.submit_main_search()
        category_count = self.page.get_total_count()
        self.assertGreaterEqual(total_count, category_count)
        self.page.click_select_subcategory()
        self.page.select_subcategory()
        self.page.submit_main_search()
        subcategory_count = self.page.get_total_count()
        self.assertGreaterEqual(category_count, subcategory_count)

    def test_question_ask_text(self):
        self.page.open_search_page()
        self.page.input_in_main_search(self.TEST_TEXT)
        self.page.submit_main_search()
        self.page.click_ask_more_button()
        question_text = self.page.get_question_input_text()
        self.assertEqual(self.TEST_TEXT, question_text)

    @classmethod
    def tearDownClass(cls):
        SearchTests.browser.quit()
