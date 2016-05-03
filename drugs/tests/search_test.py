# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from drugs.pages.drugs_page import DrugsPage
from selenium.webdriver import DesiredCapabilities, Remote


class DrugsSearchTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = DrugsPage(self.driver)
        self.page.open()
        self.search_form = self.page.search_form

    def test_search_for_existent_drug(self):
        query = u'ВИЗАРСИН'
        self.search_form.input(query)
        self.search_form.submit()
        drugs = self.search_form.found_drugs()
        self.assertIn(query, drugs)

    def test_search_by_eng(self):
        query = 'VIZARSIN'
        self.search_form.input(query)
        self.search_form.submit()
        drugs = self.search_form.found_drugs()
        self.assertIn(u'ВИЗАРСИН', drugs)

    def test_search_for_non_existent_drug(self):
        query = u'несуществующиетаблетки'
        self.search_form.input(query)
        self.search_form.submit()
        self.assertEquals(None, self.search_form.items())

    def tearDown(self):
        self.page.close()
        self.driver.quit()
