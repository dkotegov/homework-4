#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from tests import get_webdriver, get_credentials, PageObject, LOGIN_PAGE_URL, MessageActivities

ONE_MESSAGE = 1
THREE_MESSAGES = 3


class TestMessageActivities(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.page = MessageActivities()
        self.page.open(LOGIN_PAGE_URL)
        
        self.page.login()

    def test_move_1_messages(self):    
        messages_to_move, titles = self.page.move_n_msgs_to(ONE_MESSAGE, 'Черновики')
        self.page.go_to('Черновики')
    
        moved_correctly = self.page.check_moved_messages(titles)
    
        self.page.move_n_msgs_to(ONE_MESSAGE, 'Входящие')
        self.page.go_to('Входящие')
    
        self.assertEqual(moved_correctly, True)

    def test_move_3_messages(self):   
        messages_to_move, titles = self.page.move_n_msgs_to(THREE_MESSAGES, 'Черновики')
    
        self.page.go_to('Черновики')
    
        moved_correctly = self.page.check_moved_messages(titles)
    
        self.page.move_n_msgs_to(THREE_MESSAGES, 'Входящие')
        self.page.go_to('Входящие')
    
        self.assertEqual(moved_correctly, True)
    
    def test_move_all_messages(self):
        messages_to_move, titles = self.page.move_all_msgs_to('Черновики')
    
        self.page.go_to('Черновики')
    
        moved_correctly = self.page.check_moved_messages(titles)
    
        self.page.move_all_msgs_to('Входящие')
        self.page.go_to('Входящие')
    
        self.assertEqual(moved_correctly, True)

    def test_apply_flag_for_1(self):
        msg = self.page.apply_flag_for_n(ONE_MESSAGE, 'flag')
        first_len = len(msg)
        self.page.show_by_filter('flag')

        self.page.wait_until_content_change('С флажком')

        second_len = self.page.get_messages()[1]
        self.page.show_by_filter('all')

        self.page.wait_until_content_change('Все письма')

        self.page.apply_flag_for_n(ONE_MESSAGE, 'unflag')
        self.assertEqual(first_len, second_len)

    def test_apply_flag_for_3(self):
        msg = self.page.apply_flag_for_n(THREE_MESSAGES, 'flag')
        first_len = len(msg)
        self.page.show_by_filter('flag')

        self.page.wait_until_content_change('С флажком')

        second_len = self.page.get_messages()[1]
        self.page.show_by_filter('all')

        self.page.wait_until_content_change('Все письма')

        self.page.apply_flag_for_n(THREE_MESSAGES, 'unflag')
        self.assertEqual(first_len, second_len)

    def test_apply_flag_for_all(self):
        msg = self.page.apply_flag_for_all('flag')
        first_len = len(msg)
        self.page.show_by_filter('flag')

        self.page.wait_until_content_change('С флажком')

        second_len = self.page.get_messages()[1]
        self.page.show_by_filter('all')

        self.page.wait_until_content_change('Все письма')

        self.page.apply_flag_for_all('unflag')
        self.assertEqual(first_len, second_len)

    def test_apply_unread_for_1(self):
        msg = self.page.apply_flag_for_n(ONE_MESSAGE, 'unread')
        first_len = len(msg)
        self.page.show_by_filter('unread')

        self.page.wait_until_content_change('Непрочитанные')

        second_len = self.page.get_messages()[1]
        self.page.show_by_filter('all')

        self.page.wait_until_content_change('Все письма')

        self.page.apply_flag_for_n(ONE_MESSAGE, 'read')
        self.assertEqual(first_len, second_len)

    def test_apply_unread_for_3(self):
        msg = self.page.apply_flag_for_n(THREE_MESSAGES, 'unread')
        first_len = len(msg)
        self.page.show_by_filter('unread')

        self.page.wait_until_content_change('Непрочитанные')

        second_len = self.page.get_messages()[1]
        self.page.show_by_filter('all')

        self.page.wait_until_content_change('Все письма')

        self.page.apply_flag_for_n(THREE_MESSAGES, 'read')
        self.assertEqual(first_len, second_len)

    def test_apply_unread_for_all(self):
        msg = self.page.apply_flag_for_all('unread')
        first_len = len(msg)
        self.page.show_by_filter('unread')

        self.page.wait_until_content_change('Непрочитанные')

        second_len = self.page.get_messages()[1]
        self.page.show_by_filter('all')

        self.page.wait_until_content_change('Все письма')

        self.page.apply_flag_for_all('read')
        self.assertEqual(first_len, second_len)

    @classmethod
    def tearDownClass(self):
        self.page.close()
        self.page.driver.quit()
