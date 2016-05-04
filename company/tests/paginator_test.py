# -*- coding: utf-8 -*-
__author__ = 'niggor'
import os
import unittest
from company.pages.one_company_page import CompanyPage
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
        self.paginator = self.page.paginator

    def test_arrows(self):
        current_page = self.paginator.get_current_page()
        self.assertTrue(self.paginator.paging_next())
        self.assertEquals((current_page + 1), self.paginator.get_current_page())
        self.assertTrue(self.paginator.paging_prev())
        self.assertEquals((current_page), self.paginator.get_current_page())

    def test_arrow_prev_first_page(self):
        self.assertFalse(self.paginator.paging_prev())

    def test_arrow_next_last_page(self):
        self.paginator.go_to_page(self.paginator.get_last_page())
        self.assertFalse(self.paginator.paging_next())

    def test_paging(self):
        self.assertTrue(self.paginator.go_to_page(2))
        self.assertTrue(self.paginator.go_to_page(5))
        self.assertFalse(self.paginator.go_to_page(25))

    def tearDown(self):
        self.page.close()
        self.driver.quit()

