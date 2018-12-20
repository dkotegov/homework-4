#!/usr/bin/python


import unittest
from time import sleep
from src.ax import InitPage, HeaderObject, MainViewObject, SECRET_PAGE_URL, LOGIN_PAGE_URL


class TestFilters(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.page = InitPage()

        self.page.open(LOGIN_PAGE_URL)
        self.page.login()

        self.page.open(SECRET_PAGE_URL)
        self.page.click_inbox()

    def test_example(self):
        header = self.page.get_header_page_object()
        main = self.page.get_main_page_object()

        messages, count = main.get_messages()
        print count
        print '\t' + '\n\t'.join([str(m) for m in messages])
        

        header.click_filter_on_search('unread')
        header.click_filter_on_search('attach')
        
        messages, count = main.get_messages()
        print count
        print '\t' + '\t\n'.join([str(m) for m in messages])
        
        

    @classmethod
    def tearDownClass(self):
        self.page.close()
        self.page.driver.quit()


    

