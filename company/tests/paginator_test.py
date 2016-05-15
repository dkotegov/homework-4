# -*- coding: utf-8 -*-
__author__ = 'niggor'
import os
import unittest
from company.pages.list_company_page import CompanyPage
from selenium.webdriver import DesiredCapabilities, Remote


class PaginatorTest(unittest.TestCase):
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
        self.page.wait_for_another_page()
        self.assertEquals((current_page + 1), self.paginator.get_current_page())
        self.assertTrue(self.paginator.paging_prev())
        self.page.wait_for_another_page()
        self.assertEquals((current_page), self.paginator.get_current_page())

    #нельзя перейти с первой страницы назад
    def test_first_page_go_back(self):
        self.assertFalse(self.paginator.paging_prev())

    #нельзя перейти вперед с последней страницы
    def test_last_page_go_next(self):
        self.paginator.go_to_page(self.paginator.get_last_page())
        self.assertFalse(self.paginator.paging_next())

    def test_list_of_page_numbers(self):
        page_number = 2
        self.assertTrue(self.paginator.go_to_page(page_number))
        non_existent_page_number = 5
        self.assertTrue(self.paginator.go_to_page(page_number))
        self.assertFalse(self.paginator.go_to_page(non_existent_page_number))

    def tearDown(self):
    #    self.page.close()
        self.driver.quit()

