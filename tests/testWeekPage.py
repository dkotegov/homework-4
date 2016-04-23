# -*- coding: utf-8 -*-

import os

import unittest
import datetime, time

from selenium.webdriver import DesiredCapabilities, Remote


from test import auth
from test import CalendarPage


def week_calendar(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.open()

    calendar_toolbar = calendar_page.toolbar
    calendar_toolbar.choise_week()

    return calendar_page




class Tests(unittest.TestCase):
    USEREMAIL = os.environ['HW4LOGIN']
    PASSWORD = os.environ['HW4PASSWORD']


    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_week(self):
        calendar_page = CalendarPage(self.driver)
        calendar_page.open()

        calendar_toolbar = calendar_page.toolbar
        calendar_toolbar.choise_week()

        week_number = calendar_toolbar.get_week_number()

        true_week_number = datetime.datetime.now().strftime("%W")

        self.assertEqual(true_week_number, week_number)

    def test_navigation(self):
        calendar_page = CalendarPage(self.driver)
        header = calendar_page.navigation_header

        # Test next week
        header.next_week()
        calendar_toolbar = calendar_page.toolbar
        time.sleep(1)
        week_number = int(calendar_toolbar.get_week_number())
        true_week_number = int(datetime.datetime.now().strftime("%W")) + 1
        self.assertEqual(true_week_number, week_number)

        # Test true week
        header.prev_week()
        calendar_toolbar = calendar_page.toolbar
        time.sleep(1)
        week_number = calendar_toolbar.get_week_number()
        true_week_number = datetime.datetime.now().strftime("%W")
        self.assertEqual(true_week_number, week_number)

    def test_preferences(self):
        calendar_page = CalendarPage(self.driver)
        preferences = calendar_page.navigation_header_preferences

        # Open preferences
        preferences.open()
        check_open = preferences.check_open()
        self.assertEqual(True, check_open)

        # Close preferences
        preferences.close()
        check_close = preferences.check_open()
        self.assertEqual(False, check_close)

    TITLE = 'PYTHON DYE'
    NEW_TITLE = 'PYTHON BURN IN HELL'
    FRIEND_EMAIL = 'aaaaaaaaaaaaaa_aaaaaaaa_aaaaaaa@bk.ru'
    FRIEND_NAME = u'AAAAAAAAAAAAAA AAAAAAAAAAAAAA'
    DESCRIPTION = 'I HATE PYTHON'

    def test_add_event(self):
        calendar_page = CalendarPage(self.driver)
        table = calendar_page.calendar_table

        table.open_new_event_week()
        table.set_title(self.TITLE)
        table.add_friend(self.FRIEND_EMAIL)
        table.submit()

        table.check_event(self.TITLE)
        table.check_title(self.TITLE)

        check_friend_name = table.check_friend_name()
        self.assertEqual(self.FRIEND_NAME, check_friend_name)

        table.del_event()

    def test_add_event_with_extra_options(self):
        calendar_page = CalendarPage(self.driver)
        table = calendar_page.calendar_table

        table.open_new_event_week()
        table.set_title(self.TITLE)
        table.extra_options(self.DESCRIPTION)
        table.submit()

        # Like assert
        table.check_event(self.TITLE)
        table.check_title(self.TITLE)
        table.check_description(self.DESCRIPTION)

        table.del_event()

    def test_edit_event(self):
        calendar_page = CalendarPage(self.driver)
        table = calendar_page.calendar_table

        table.open_new_event_week()
        table.set_title(self.TITLE)
        table.add_friend(self.FRIEND_EMAIL)
        table.submit()

        table.check_event(self.TITLE)
        table.click_edit()
        table.set_title(self.NEW_TITLE)
        table.submit()

        # Like assert
        table.check_event(self.NEW_TITLE)
        table.check_title(self.NEW_TITLE)
