# -*- coding: utf-8 -*-

from base_test import BaseTest
from pages import MainPage, SearchPage


class BaseSearchInputTest(BaseTest):
    DEFAULT_SEARCH_STRING = 'kek'

    def setUp(self):
        super(BaseSearchInputTest, self).setUp()

        self.main_page = MainPage(self.driver)
        self.main_page.search(self.DEFAULT_SEARCH_STRING)


class SearchInputPopupTest(BaseSearchInputTest):
    def test(self):
        self.assertIsNotNone(self.main_page.get_search_suggestions_on_page())


class SearchInputOverlayTest(BaseSearchInputTest):
    def test(self):
        self.assertIsNotNone(self.main_page.get_search_overlay_on_page())


class SearchInputSuggestionsShowAllTest(BaseSearchInputTest):
    SHOWALL_TEXT = u'Показать все результаты'

    def test(self):
        self.assertEqual(self.SHOWALL_TEXT,
            self.main_page.get_search_suggestions_showall_text())


class SearchInputSubmitTest(BaseSearchInputTest):
    MENU_LENGTH = 5

    def test(self):
        self.main_page.submit_search()

        search_page = SearchPage(self.driver)
        menu = search_page.get_menu()
        self.assertEqual(self.MENU_LENGTH, len(menu))
