#!/usr/bin/python


import unittest
from time import sleep
from tests import get_webdriver, get_credentials, InitPage, HeaderObject, SECRET_PAGE_URL, LOGIN_PAGE_URL


class TestFilters(unittest.TestCase):
    
    def setUp(self):
        self.page = InitPage()

        self.page.open(LOGIN_PAGE_URL)
        self.page.login()

        self.page.open(SECRET_PAGE_URL)
        self.page.click_inbox()

    def test_example(self):
        header = self.page.get_header_page_object()
        header.click_filter_on_search('unread')
        header.click_filter_on_search('attach')
        sleep(2)

    def tearDown(self):
        self.page.close()
    

