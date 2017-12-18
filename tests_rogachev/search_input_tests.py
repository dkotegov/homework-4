# -*- coding: utf-8 -*-

import unittest

from base_test import BaseTest
from pages import MainPage


class BaseSearchInputTest(BaseTest):
    DEFAULT_SEARCH_STRING = 'test'

    def setUp(self):
        super(BaseSearchInputTest, self).setUp()

        self.main_page = MainPage(self.driver)
        self.main_page.search(self.DEFAULT_SEARCH_STRING)


class SearchInputSuggestionsShowAllTest(BaseSearchInputTest):
    SHOW_ALL_TEXT = u'Показать все результаты'

    def test(self):
        self.assertEqual(self.SHOW_ALL_TEXT, self.main_page.get_search_suggestions_showall_text())


class SearchInputSubmitTest(BaseSearchInputTest):

    def test(self):
        self.main_page.submit_search()
        self.assertTrue(self.DEFAULT_SEARCH_STRING in self.driver.current_url)


search_input_tests = [
    unittest.TestSuite((
        unittest.makeSuite(SearchInputSuggestionsShowAllTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(SearchInputSubmitTest),
    )),
]
