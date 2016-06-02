# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from drugs.pages.drugs_page import DrugsPage

from selenium.webdriver import DesiredCapabilities, Remote


class CatalogTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = DrugsPage(self.driver)
        self.page.open()
        self.catalog = self.page.catalog

    def test_check_link(self):
        for link in self.catalog.links():
            self.assertTrue(self.catalog.check_link(link))

    def test_check_redirect(self):
        text = u"Витамины"
        self.catalog.to_link(text)
        #self.page.wait_for_another_page()
        self.assertEquals(text, self.page.get_title())
        self.driver.back()
        text = u"Миорелаксанты"
        self.catalog.to_link(text)
        #self.page.wait_for_another_page()
        self.assertEquals(text, self.page.get_title())

    def tearDown(self):
        #self.page.close()
        self.driver.quit()
