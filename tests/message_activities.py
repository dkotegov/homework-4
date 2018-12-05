#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import time

from tests import get_webdriver, get_credentials, PageObject, LOGIN_PAGE_URL, MessageActivities


class TestMessageActivities(unittest.TestCase):

    def setUp(self):
        self.page = MessageActivities()
        self.page.open(LOGIN_PAGE_URL)
        self.page.login()

    # def test_move_3_messages(self):
    #     n = 3
    #
    #     messages_to_move, titles = self.page.move_n_msgs_to(n, 'Черновики')
    #     print 'messages_to_move: ',  messages_to_move
    #     print 'titles: ', titles
    #
    #     self.page.go_to('Черновики')
    #
    #     moved_correctly = self.page.check_moved_messages(titles)
    #
    #     self.page.move_n_msgs_to(n, 'Входящие')
    #     self.page.go_to('Входящие')
    #
    #     self.assertEqual(moved_correctly, True)
    #
    # def test_move_all_messages(self):
    #     messages_to_move, titles = self.page.move_all_msgs_to('Черновики')
    #     print 'messages_to_move: ',  messages_to_move
    #     print 'titles: ', titles
    #
    #     self.page.go_to('Черновики')
    #
    #     moved_correctly = self.page.check_moved_messages(titles)
    #
    #     self.page.move_all_msgs_to('Входящие')
    #     self.page.go_to('Входящие')
    #
    #     self.assertEqual(moved_correctly, True)

    def test_apply_flag(self):
        msg = self.page.apply_flag_for_all('flag')
        self.page.unflag('flag', msg)


        time.sleep(2)

    def tearDown(self):
        self.page.close()
