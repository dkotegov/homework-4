#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver


class RealtyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        #self.addCleanup(self.browser.quit)

    def tearDown(self):
        self.browser.quit()

    # def testPageTitle(self):
    #     self.browser.get('https://realty.mail.ru/')
    #     self.assertIn(u'Продажа и аренда недвижимости - Недвижимость Mail.Ru', self.browser.title)

    def testPageTitle(self):
        self.browser.get('https://msk.realty.mail.ru/offer/sale-liv-3074150216334851.html?osale2')
        self.assertIn(u'3-комн. квартира, пр-кт. Вернадского, д.92', self.browser.title)
        slider = Slider(self.browser)
        slider.open_slider()
        slider.click_next()
        slider.click_prev()
        num = slider.get_num_of_photo()
        slider.close_slider()


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class Slider(Component):

    def open_slider(self):
        slider = self.driver.find_element_by_class_name("photo__action")
        slider.click()

    def close_slider(self):
        btn_close = self.driver.find_element_by_class_name("viewbox__close")
        btn_close.click()

    def click_next(self):
        btn_next = self.driver.find_element_by_class_name("icon_control_next")
        btn_next.click()

    def click_prev(self):
        btn_prev = self.driver.find_element_by_class_name("icon_control_previous")
        btn_prev.click()

    def get_num_of_photo(self):
        current_num = self.driver.find_element_by_class_name("viewbox__current")
        return current_num.text

if __name__ == '__main__':
    unittest.main(verbosity=2)
