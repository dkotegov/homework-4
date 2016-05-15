# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from drugs.pages.one_drug_page import DrugPage

from selenium.webdriver import DesiredCapabilities, Remote


class CounterTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = DrugPage(self.driver, 'vizarsin')
        self.page.open()
        self.counter = self.page.counter

    def test_counter_visible(self):
        self.assertFalse(self.counter.counter_is_visible())
        self.counter.to_order()
        self.counter.selected_dropdown_item_by_number(1)
        self.assertTrue(self.counter.counter_is_visible())

    def test_counter(self):
        self.page.login()
        self.counter.to_order()
        self.counter.selected_dropdown_item_by_number(1)
        self.assertEquals(1, int(self.counter.get_counter_value()))
        self.counter.increment()
        self.counter.increment()
        self.assertEquals(3, int(self.counter.get_counter_value()))
        self.counter.decrement()
        self.assertEquals(2, int(self.counter.get_counter_value()))

    def test_counter_in_basket(self):
        self.page.login()
        self.counter.to_order()
        self.counter.selected_dropdown_item_by_number(1)
        self.counter.do_order()
        self.page.wait_for_another_page()
        self.assertEquals(1, int(self.counter.get_counter_value()))
        self.driver.back()
        self.counter.increment()
        self.counter.increment()
        self.counter.do_order()
        self.page.wait_for_another_page()
        self.assertEquals(3, int(self.counter.get_counter_value()))
        self.driver.back()
        self.counter.decrement()
        self.counter.do_order()
        self.page.wait_for_another_page()
        self.assertEquals(2, int(self.counter.get_counter_value()))

    def test_negative_counter_value(self):
        self.counter.to_order()
        self.counter.selected_dropdown_item_by_number(1)
        self.counter.decrement()
        self.assertFalse(self.counter.counter_is_visible())

    def test_check_type(self):
        self.page.login()
        self.counter.to_order()
        types = self.counter.dropdown_items()
        for t in types:
            self.counter.selected_dropdown_item(t)
            self.counter.do_order()
            self.page.wait_for_another_page()
            self.assertEquals(t, self.counter.result_type())
            self.driver.back()
            self.counter.decrement()
            self.counter.to_order()

    def tearDown(self):
        #self.page.close()
        self.driver.quit()
