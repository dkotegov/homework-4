#!/usr/bin/python


import unittest
from src.ax import InitPage, HeaderObject, MainViewObject, SECRET_PAGE_URL, LOGIN_PAGE_URL


class TestFilters(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.page = InitPage()

        self.page.open(LOGIN_PAGE_URL)
        self.page.login()

        self.page.open(SECRET_PAGE_URL)
        self.page.click_inbox()

    def test_filters(self):
        header = self.page.get_header_page_object()
        main = self.page.get_main_page_object()

        messages, _ = main.get_messages()
        expected = list(filter(
            lambda m: m.is_unread() and m.has_attach(),
            messages
        ))

        header.click_filter_on_search('unread')
        header.click_filter_on_search('attach')
        
        messages, _ = main.get_messages()

        self.assertEqual(len(expected), len(messages))
        for msg in messages:
            self.assertIn(msg, expected)
        
        

    @classmethod
    def tearDownClass(self):
        self.page.close()
        self.page.driver.quit()


    

