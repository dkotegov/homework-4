# -*- coding: utf-8 -*-
__author__ = 'niggor'
import os
import unittest
from company.pages.companies_page import CompaniesPage
from selenium.webdriver import DesiredCapabilities, Remote


class CompanyListTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = CompaniesPage(self.driver)
        self.page.open()
        self.list = self.page.company_list

    def test_check_links(self):
        for link in self.list.links():
            self.assertTrue(self.list.check_link(link))

    def test_check_redirect(self):
        companies = self.list.get_all_companies()
        for i in companies:
            self.list.go_to_company_page(i)
            self.page.wait_for_another_page()
            expected_title = i + u" в Москве"
            self.assertEquals(expected_title, self.page.get_title())
            self.driver.back()

    def tearDown(self):
        self.page.close()
        self.driver.quit()
