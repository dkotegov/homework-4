# -*- coding: utf-8 -*-
__author__ = 'niggor'
import os
import unittest
from company.pages.list_company_page import CompanyPage
from selenium.webdriver import DesiredCapabilities, Remote


class CompanySearchTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = CompanyPage(self.driver)
        self.page.open()
        self.dropdown_list = self.page.dropdown_list

    def test_scroll(self):
        list_element = u'Бауманская'
        self.page.dropdown_list.open_dropdown_list()
        self.assertFalse(self.dropdown_list.element_is_visible(list_element))
        self.dropdown_list.scroll(list_element)
        self.assertTrue(self.dropdown_list.element_is_visible(list_element))

    def test_dropdown_list_value(self):
        metro_station = u'Бауманская'
        self.assertEquals(u'Любое метро', self.dropdown_list.get_value())
        self.page.dropdown_list.open_dropdown_list()
        self.dropdown_list.select_metro_station(metro_station)
        self.assertEquals(metro_station, self.dropdown_list.get_value())

    def test_selection_metro_stations(self):
        metro_station = u'Бауманская'
        self.page.dropdown_list.open_dropdown_list()
        self.dropdown_list.select_metro_station(metro_station)

    def tearDown(self):
        self.page.close()
        self.driver.quit()

