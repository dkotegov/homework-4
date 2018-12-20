#!/usr/bin/python


import unittest

from tests import get_webdriver, get_credentials, FiltersApplyingPageObject, SECRET_PAGE_URL, LOGIN_PAGE_URL

@unittest.skip
class TestApplyingFilters(unittest.TestCase):
    
    def setUp(self):
        self.page = FiltersApplyingPageObject()

    def test_example(self):
        self.page.open(LOGIN_PAGE_URL)
        self.page.login()

        self.page.open(SECRET_PAGE_URL)
        self.page.click_inbox()

        self.page.click_filter_flag()

        #self.page.click_to_search_panel()

        
        self.assertEqual(self.page.state, None)

    def tearDown(self):
        self.page.close()
    

