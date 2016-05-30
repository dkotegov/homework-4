# -*- coding: utf-8 -*-
import os

from selenium.webdriver import Remote, DesiredCapabilities
import datetime
import random
from pages.pages import BirthPage
import unittest
import urlparse

MONTHS = [u'Декабрь', u'Январь', u'Февраль', u'Март', u'Апрель', u'Май', u'Июнь', u'Июль',
          u'Август', u'Сентябрь', u'Октябрь', u'Ноябрь', u'Декабрь', u'Январь', 'Февраль']

TRUE_MONTHS = [u'декабря', u'января', u'февраля', u'марта', u'апреля', u'мая', u'июня', u'июля',
               u'августа', u'сентября', u'октября', u'Ноября', u'декабря', u'января', 'февраля']


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()


class BirthPageTestCase(BaseTestCase):
    def test_initial_url(self):
        page = BirthPage(self.driver)
        page.open()
        self.assertEqual(self.driver.current_url, urlparse.urljoin(page.BASE_URL, page.PATH))

    def test_header_calendar_existance(self):
        page = BirthPage(self.driver)
        page.open()
        self.assertIsNotNone(page.header_block.calendar)

    def test_calendar_dropdown_open_function(self):
        page = BirthPage(self.driver)
        page.open()
        page.header_block.click_calendar_dropdown_button()
        self.assertTrue(page.header_block.calendar_dropdown_box_visible())

    def test_calendar_dropdown_close_function(self):
        page = BirthPage(self.driver)
        page.open()
        page.header_block.click_calendar_dropdown_button()
        page.header_block.click_calendar_dropdown_button()
        self.assertFalse(page.header_block.calendar_dropdown_box_visible())

    def test_current_calendar_month(self):
        page = BirthPage(self.driver)
        page.open()
        page.header_block.click_calendar_dropdown_button()
        self.assertEqual(page.header_block.today_month, MONTHS[datetime.date.today().month])

    def test_next_month_button(self):
        page = BirthPage(self.driver)
        page.open()
        page.header_block.click_calendar_dropdown_button()
        page.header_block.click_next_month_button()
        self.assertEqual(page.header_block.today_month, MONTHS[datetime.date.today().month + 1])

    def test_previous_month_button(self):
        page = BirthPage(self.driver)
        page.open()
        page.header_block.click_calendar_dropdown_button()
        page.header_block.click_previous_month_button()
        self.assertEqual(page.header_block.today_month, MONTHS[datetime.date.today().month - 1])

    def test_set_month(self):
        page = BirthPage(self.driver)
        page.open()
        page.header_block.click_calendar_dropdown_button()
        page.header_block.click_previous_month_button()
        page.header_block.click_previous_month_button()
        old_month = page.header_block.today_month
        page.header_block.click_calendar_dropdown_button()
        page.header_block.click_calendar_dropdown_button()
        self.assertEqual(page.header_block.today_month, old_month)

    def test_month_search(self):
        page = BirthPage(self.driver)
        page.open()
        page.header_block.click_calendar_dropdown_button()
        day = random.randint(1, 9)
        month = datetime.date.today().month
        page.header_block.click_day(day, month)
        page.user_list_block.click_first_item()
        self.assertEqual(str(day), page.user_list_block.get_item_info()[0])

    def test_random_date_search(self):
        page = BirthPage(self.driver)
        page.open()
        page.header_block.click_calendar_dropdown_button()
        day = random.randint(1, 9)
        month = datetime.date.today().month
        page.header_block.click_day(day, month)
        page.user_list_block.click_first_item()
        self.assertEqual(TRUE_MONTHS[month], page.user_list_block.get_item_info()[1])
