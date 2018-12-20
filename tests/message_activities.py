#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import time

from tests import get_webdriver, get_credentials, PageObject, LOGIN_PAGE_URL, MessageActivities


class TestMessageActivities(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.page = MessageActivities()
        self.page.open(LOGIN_PAGE_URL)
        self.page.login()

    def test_move_1_messages(self):
        n = 1
    
        messages_to_move, titles = self.page.move_n_msgs_to(n, 'Черновики')
        print 'messages_to_move: ',  messages_to_move
        print 'titles: ', titles
    
        self.page.go_to('Черновики')
    
        moved_correctly = self.page.check_moved_messages(titles)
    
        self.page.move_n_msgs_to(n, 'Входящие')
        self.page.go_to('Входящие')
    
        self.assertEqual(moved_correctly, True)

    def test_move_3_messages(self):
        n = 3
    
        messages_to_move, titles = self.page.move_n_msgs_to(n, 'Черновики')
        print 'messages_to_move: ',  messages_to_move
        print 'titles: ', titles
    
        self.page.go_to('Черновики')
    
        moved_correctly = self.page.check_moved_messages(titles)
    
        self.page.move_n_msgs_to(n, 'Входящие')
        self.page.go_to('Входящие')
    
        self.assertEqual(moved_correctly, True)
    
    def test_move_all_messages(self):
        messages_to_move, titles = self.page.move_all_msgs_to('Черновики')
        print 'messages_to_move: ',  messages_to_move
        print 'titles: ', titles
    
        self.page.go_to('Черновики')
    
        moved_correctly = self.page.check_moved_messages(titles)
    
        self.page.move_all_msgs_to('Входящие')
        self.page.go_to('Входящие')
    
        self.assertEqual(moved_correctly, True)

    def test_apply_flag_for_1(self):
        msg = self.page.apply_flag_for_n(1, 'flag')
        first_len = len(msg)
        self.page.show_by_filter('flag')

        self.page.wait_until_content_change('С флажком')

        second_len = self.page.get_messages()[1]
        self.page.show_by_filter('all')

        self.page.wait_until_content_change('Все письма')

        self.page.apply_flag_for_n(1, 'unflag')
        self.assertEqual(first_len, second_len)

    def test_apply_flag_for_3(self):
        msg = self.page.apply_flag_for_n(3, 'flag')
        first_len = len(msg)
        self.page.show_by_filter('flag')

        self.page.wait_until_content_change('С флажком')

        second_len = self.page.get_messages()[1]
        self.page.show_by_filter('all')

        self.page.wait_until_content_change('Все письма')

        self.page.apply_flag_for_n(3, 'unflag')
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
        msg = self.page.apply_flag_for_n(1, 'unread')
        first_len = len(msg)
        self.page.show_by_filter('unread')

        self.page.wait_until_content_change('Непрочитанные')

        second_len = self.page.get_messages()[1]
        self.page.show_by_filter('all')

        self.page.wait_until_content_change('Все письма')

        self.page.apply_flag_for_n(1, 'read')
        self.assertEqual(first_len, second_len)

    def test_apply_unread_for_3(self):
        msg = self.page.apply_flag_for_n(3, 'unread')
        first_len = len(msg)
        self.page.show_by_filter('unread')

        self.page.wait_until_content_change('Непрочитанные')

        second_len = self.page.get_messages()[1]
        self.page.show_by_filter('all')

        self.page.wait_until_content_change('Все письма')

        self.page.apply_flag_for_n(3, 'read')
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
        self.driver.quit()

