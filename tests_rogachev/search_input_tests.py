# -*- coding: utf-8 -*-

from base_test import BaseTest
from pages import MainPage


class BaseSearchInputTest(BaseTest):
    DEFAULT_SEARCH_STRING = 'test'

    def setUp(self):
        super(BaseSearchInputTest, self).setUp()

        self.main_page = MainPage(self.driver)
        self.main_page.search(self.DEFAULT_SEARCH_STRING)


class SearchInputSubmitTest(BaseSearchInputTest):

    def test(self):
        self.main_page.submit_search()
        self.assertIn(self.DEFAULT_SEARCH_STRING, self.driver.current_url)
