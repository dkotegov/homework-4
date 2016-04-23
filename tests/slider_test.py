# -*- coding: utf-8 -*-
import os
import unittest
import urlparse

from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver import DesiredCapabilities, Remote


class Page(object):
    BASE_URL = 'http://msk.realty.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class SalePage(Page):
    PATH = '/sale/living/'

    @property
    def first_offer(self):
        return PageOffer(self.driver)


class PageOffer(SalePage):
    CLASS_TITLE = 'p-instance__title'

    def open(self):
        super(PageOffer, self).open()
        title_links = self.driver.find_elements_by_class_name(self.CLASS_TITLE)
        link = title_links[2].get_attribute('href')
        self.driver.get(link)

    @property
    def slider(self):
        return Slider(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class Slider(Component):
    OPEN_CLASS = 'photo__action'
    CLOSE_CLASS = 'viewbox__close'
    ICON_NEXT = 'icon_control_next'
    ICON_PREV = 'icon_control_previous'
    BOX_NEXT = 'viewbox__control_next'
    BOX_PREV = 'viewbox__control_previous'
    CURRENT_NUM = 'viewbox__current'
    TOTAL_NUM = 'viewbox__total'

    def __init__(self, driver):
        super(Slider, self).__init__(driver)
        self.page_num = 0

    def open_slider(self):
        slider = self.driver.find_element_by_class_name(self.OPEN_CLASS)
        slider.click()
        self.page_num = 1

    def close_slider(self):
        btn_close = self.driver.find_element_by_class_name(self.CLOSE_CLASS)
        btn_close.click()
        self.page_num = 0

    def click_next(self, method=0):
        btn_next = self.driver.find_element_by_class_name(self.ICON_NEXT)
        if method:
            btn_next = self.driver.find_element_by_class_name(self.BOX_NEXT)
        btn_next.click()
        self.page_num += 1

    def click_prev(self, method=0):
        btn_prev = self.driver.find_element_by_class_name(self.ICON_PREV)
        if method:
            btn_prev = self.driver.find_element_by_class_name(self.BOX_PREV)
        btn_prev.click()
        self.page_num -= 1

    def get_page_num(self):
        return self.page_num

    def get_page_num_from_browser(self):
        current_num = self.driver.find_element_by_class_name(self.CURRENT_NUM)
        return int(current_num.text)

    def get_max_page_num(self):
        max_num = self.driver.find_element_by_class_name(self.TOTAL_NUM)
        return int(max_num.text)


class ChareBlock(Component):
    BUTTONS_CLASSES = ['share_vk', 'share_fb', 'share_ok', 'share_my', 'share_tw']

    def click_btn(self, btn_class):
        btn = self.driver.find_element_by_class_name(btn_class)
        btn.click()

    def click_all_btn(self):
        for class_btn in self.BUTTONS_CLASSES:
            self.click_btn(class_btn)


class RealtyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = os.environ.get('HW4BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, self.browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def testPageTitle(self):
        offer_page = PageOffer(self.driver)
        offer_page.open()
        slider = offer_page.slider
        slider.open_slider()
        slider.click_next()
        slider.click_next(1)
        slider.click_prev()
        slider.click_prev(1)
        
        self.assertEqual(slider.get_page_num(), slider.get_page_num_from_browser())
        # проверяем наличие всех кнопок для соц.сетей
        chare_block = ChareBlock(self.driver)
        chare_block.click_all_btn()

        # проверка, что у первого элемента нет перехода назад
        with self.assertRaises(ElementNotVisibleException):
            slider.click_prev()
        
        # проверка, что у первого элемента нет перехода вперед
        all_photos_num = slider.get_max_page_num()
        for i in range(1, all_photos_num):
            slider.click_next()
        with self.assertRaises(ElementNotVisibleException):
            slider.click_next()
        
        slider.close_slider()