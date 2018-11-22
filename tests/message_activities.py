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

        n = 3

        messages_to_move = self.page.move_n_msgs_to(n, 'Спам')
        
        self.page.go_to('Спам')
        # time.sleep(1)

        moved_correctly = self.page.check_moved_messages(messages_to_move)

        self.page.move_n_msgs_to(n, 'Входящие')
        self.page.go_to('Входящие')

        time.sleep(2)

        self.assertEqual(moved_correctly, True)
    

    def tearDown(self):
        self.page.close()
    

