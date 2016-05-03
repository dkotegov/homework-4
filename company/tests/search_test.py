# -*- coding: utf-8 -*-
__author__ = 'niggor'
import os
import unittest
from company.pages.companies_page import CompaniesPage
from selenium.webdriver import DesiredCapabilities, Remote

class CompanySearchTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = CompaniesPage(self.driver)
        self.page.open()
        self.search = self.page.search

    def test_search_existing_companies(self):
        query = u'Аптека'
        self.search.input(query)
        self.search.submit()
        self.page.wait_for_another_page()
        self.assertNotEqual(0, len(self.search.found_companies()))

    def test_search_non_existent(self):
        query = u'aaaaaaaaaaaa'
        self.search.input(query)
        self.search.submit()
        self.page.wait_for_another_page()
        self.assertEqual(0, len(self.search.found_companies()))

    def tearDown(self):
        self.page.close()
        self.driver.quit()

