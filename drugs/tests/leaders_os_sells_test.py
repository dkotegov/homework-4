# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from drugs.pages.drugs_page import DrugssPage
from selenium.webdriver import DesiredCapabilities, Remote

class MedicamentsTestLeadersOfSellsTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = DrugssPage(self.driver)
        self.page.open()
        self.drugs = self.page.leaders_of_sells

    def test_check_redirect(self):
        drags_names = self.drugs.get_all()
        for name in drags_names:
            self.drugs.go_to_drugs_page(name)
            self.page.wait_for_another_page()
            self.assertEquals(name, self.page.get_title())
            self.driver.back()

    def tearDown(self):
        self.page.close()
        self.driver.quit()
