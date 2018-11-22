#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import time

from tests import get_webdriver, get_credentials, PageObject, LOGIN_PAGE_URL, MessageActivities


class TestMessageActivities(unittest.TestCase):
    
    def setUp(self):
        self.page = MessageActivities()

    def test_example(self):
        self.page.open(LOGIN_PAGE_URL)
        self.page.login()
        
        self.page.move_all_msgs('Спам')

        self.page.go_to('Спам')

        time.sleep(3)

        self.page.move_all_msgs('Входящие')
    

    def tearDown(self):
        self.page.close()
    

