# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver


class RealtyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        #self.addCleanup(self.browser.quit)

    def tearDown(self):
        self.browser.quit()

    def testPageTitle(self):
        offer_page = PageOffer(self.browser)
        offer_page.open_page()
        slider = Slider(self.browser)
        slider.open_slider()
        slider.click_next()
        slider.click_prev()
        self.assertEqual(slider.get_page_num(), slider.get_page_num_from_browser())
        slider.close_slider()


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class Slider(Component):

    def __init__(self, driver):
        super(Slider, self).__init__(driver)
        self.page_num = 0


    def open_slider(self):
        slider = self.driver.find_element_by_class_name("photo__action")
        slider.click()
        self.page_num = 1

    def close_slider(self):
        btn_close = self.driver.find_element_by_class_name("viewbox__close")
        btn_close.click()
        self.page_num = 0

    def click_next(self):
        btn_next = self.driver.find_element_by_class_name("icon_control_next")
        btn_next.click()
        self.page_num += 1

    def click_prev(self):
        btn_prev = self.driver.find_element_by_class_name("icon_control_previous")
        btn_prev.click()
        self.page_num -= 1

    def get_page_num(self):
        return self.page_num

    def get_page_num_from_browser(self):
        current_num = self.driver.find_element_by_class_name("viewbox__current")
        return int(current_num.text)


class PageOffer(Component):

    def open_page(self):
        self.driver.get('https://msk.realty.mail.ru/sale/living/')
        title_links = self.driver.find_elements_by_class_name('p-instance__title')
        link = title_links[2].get_attribute('href')
        self.driver.get(link)

