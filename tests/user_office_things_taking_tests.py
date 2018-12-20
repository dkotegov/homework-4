# -*- coding: utf-8 -*-

import os
import random
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.admin_page import AdminPage
from tests.pages.user_page import UserPage


class UserOfficeThingsTakingTests(unittest.TestCase):
    USER_NAME = "userMaxim"
    USER_PASSWORD = "qwerty123"

    SRC_NAME = "Laptop"
    SRC_DESCRIPTION = "ThinkPad T430p"

    SRC_NUM_ALL = 5
    SRC_NUM_FOR_TAKING = 1

    get_ok_msg = "Taking source success."
    get_not_enough_msg = "Not enough source."

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.admin_page = AdminPage(self.driver)
        self.admin_page.open()
        self.admin_page.add_user(self.USER_NAME, self.USER_PASSWORD)
        src_id = 1000 + int(random.random() * 1000)
        self.admin_page.add_source(self.SRC_NAME, self.SRC_DESCRIPTION, self.SRC_NUM_ALL, src_id)

        self.user_page = UserPage(self.driver)
        self.user_page.open()

        self.user_page.sign_in(self.USER_NAME, self.USER_PASSWORD)

        self.all_things_list = self.user_page.all_things_list
        self.my_things_list = self.user_page.my_things_list

    def tearDown(self):
        self.admin_page.open()
        self.admin_page.reset()
        self.driver.quit()

    def test_things_take_ok(self):
        self.user_page.goto_all_things()
        alert_text = self.all_things_list.take_num_of_last_thing(self.SRC_NUM_FOR_TAKING)

        self.assertEqual(alert_text, self.get_ok_msg)

    def test_things_take_too_much(self):
        self.user_page.goto_all_things()
        alert_text = self.all_things_list.take_num_of_last_thing(self.SRC_NUM_ALL + 1)

        self.assertEqual(alert_text, self.get_not_enough_msg)

    def test_things_take_add_ok_to_my_things_list(self):
        self.user_page.goto_my_things()
        start_number = self.my_things_list.get_number_of_things_in_list()

        self.user_page.goto_all_things()
        self.all_things_list.take_num_of_last_thing(self.SRC_NUM_FOR_TAKING)

        self.user_page.goto_my_things()
        current_number = self.my_things_list.get_number_of_things_in_list()

        self.assertAlmostEqual(start_number, current_number, self.SRC_NUM_FOR_TAKING)

    def test_things_take_add_too_much_to_my_things_list(self):
        self.user_page.goto_my_things()
        start_number = self.my_things_list.get_number_of_things_in_list()

        self.user_page.goto_all_things()
        self.all_things_list.take_num_of_last_thing(self.SRC_NUM_ALL + 1)

        self.user_page.goto_my_things()
        current_number = self.my_things_list.get_number_of_things_in_list()

        self.assertAlmostEqual(start_number, current_number, 0)

    def test_all_things_counter_of_thing_increase_after_ok_taking(self):
        self.user_page.goto_all_things()
        start_counter = self.all_things_list.get_counter_of_last_thing()

        self.all_things_list.take_num_of_last_thing(self.SRC_NUM_FOR_TAKING)
        self.user_page.goto_my_things()
        self.user_page.goto_all_things()
        current_counter = self.all_things_list.get_counter_of_last_thing()

        self.assertEqual(current_counter, start_counter - self.SRC_NUM_FOR_TAKING)

    def test_all_things_counter_of_thing_not_increase_after_too_much_taking(self):
        self.user_page.goto_all_things()
        start_counter = self.all_things_list.get_counter_of_last_thing()

        self.all_things_list.take_num_of_last_thing(self.SRC_NUM_ALL + 1)
        current_counter = self.all_things_list.get_counter_of_last_thing()

        self.assertEqual(current_counter, start_counter)

    def test_my_things_counter_of_thing_increase_after_ok_taking(self):
        self.user_page.goto_all_things()
        self.all_things_list.take_num_of_last_thing(self.SRC_NUM_FOR_TAKING)

        self.user_page.goto_my_things()
        start_counter = self.my_things_list.get_counter_of_last_thing()

        self.user_page.goto_all_things()
        self.all_things_list.take_num_of_last_thing(self.SRC_NUM_FOR_TAKING)

        self.user_page.goto_my_things()
        current_counter = self.my_things_list.get_counter_of_last_thing()

        self.assertEqual(current_counter, start_counter + self.SRC_NUM_FOR_TAKING)

    def test_my_things_counter_of_thing_not_increase_after_too_much_taking(self):
        self.user_page.goto_all_things()
        self.all_things_list.take_num_of_last_thing(self.SRC_NUM_FOR_TAKING)

        self.user_page.goto_my_things()
        start_counter = self.my_things_list.get_counter_of_last_thing()

        self.user_page.goto_all_things()
        self.all_things_list.take_num_of_last_thing(self.SRC_NUM_ALL)

        self.user_page.goto_my_things()
        current_counter = self.my_things_list.get_counter_of_last_thing()

        self.assertEqual(current_counter, start_counter)
