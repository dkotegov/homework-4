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
        calendar_page = CalendarPage(self.driver)
        self.table = calendar_page.calendar_table

        self.table.open_new_event_week()

    def tearDown(self):
        self.table.del_event()
        self.driver.quit()

    TITLE = 'PYTHON DYE'
    NEW_TITLE = 'PYTHON BURN IN HELL'
    FRIEND_EMAIL = 'aaaaaaaaaaaaaa_aaaaaaaa_aaaaaaa@bk.ru'
    FRIEND_NAME = u'AAAAAAAAAAAAAA AAAAAAAAAAAAAA'
    DESCRIPTION = 'I HATE PYTHON'

    def test_add_event(self):

        self.table.set_title(self.TITLE)
        self.table.add_friend(self.FRIEND_EMAIL)
        self.table.submit_week()

        self.table.check_event(self.TITLE)
        self.table.check_title(self.TITLE)

        check_friend_name = self.table.check_friend_name()
        self.assertEqual(self.FRIEND_NAME, check_friend_name)



    def test_add_event_with_extra_options(self):

        self.table.set_title(self.TITLE)
        self.table.extra_options(self.DESCRIPTION)
        self.table.submit()

        # Like assert
        self.table.check_event(self.TITLE)
        self.table.check_title(self.TITLE)
        self.table.check_description(self.DESCRIPTION)

    def test_edit_event(self):

        self.table.set_title(self.TITLE)
        self.table.add_friend(self.FRIEND_EMAIL)
        self.table.submit_week()

        self.table.check_event(self.TITLE)
        self.table.click_edit()
        self.table.set_title(self.NEW_TITLE)
        self.table.submit()

        # Like assert
        self.table.check_event(self.NEW_TITLE)
        self.table.check_title(self.NEW_TITLE)
