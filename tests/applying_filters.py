#!/usr/bin/python


import unittest

from tests import get_webdriver, get_credentials, PageObject, LOGIN_PAGE_URL


class TestApplyingFilters(unittest.TestCase):
    
    def setUp(self):
        self.page = PageObject()

    def test_example(self):
        self.page.open(LOGIN_PAGE_URL)
        self.page.login()
        
        self.assertNotEquals(self.page.state, None)


    def tearDown(self):
        self.page.close()
    

