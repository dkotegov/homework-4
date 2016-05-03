# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from drugs.pages.one_drug_page import DrugPage

from selenium.webdriver import DesiredCapabilities, Remote


class AnalogsTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = DrugPage(self.driver, 'vizarsin')
        self.page.open()
        self.analogs = self.page.analogs

    def test_analogs(self):
        drags_names = self.page.analogs.get_names()
        for name in drags_names:
            self.page.analogs.go_to_drugs_page(name)
            self.page.wait_for_another_page()
            self.assertEquals(name.split(',')[0], self.page.analogs.result_drag())
            self.driver.back()

    def tearDown(self):
        self.page.close()
        self.driver.quit()
