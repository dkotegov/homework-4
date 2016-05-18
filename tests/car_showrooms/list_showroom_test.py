import os
import time
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.car_showrooms.pages import ShowroomPage


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class ShowroomList(Component):
    __ITEM_TITLE = 'div.dealer-card__title a'
    __ITEM_PAGE_TITLE = 'span.bread__curr'
    __ITEM_ADDRESS = 'div.dealer-card__adress'
    __ITEM_PHONE = 'div.dealer-card__phone'
    __PAGINATOR_CURRENT_PARAM = "a.pager__pin.pager__pin_perpage.pager__pin_on"
    __PAGINATOR_PARAM = "a.pager__pin.pager__pin_perpage"

    def open_first_item(self):
        item_title = self.driver.find_element_by_css_selector(self.__ITEM_TITLE)
        text = item_title.text
        item_title.click()
        return text

    def get_first_item_page_title(self):
        return self.driver.find_element_by_css_selector(self.__ITEM_PAGE_TITLE).text

    def get_item_address(self):
        return self.driver.find_element_by_css_selector(self.__ITEM_ADDRESS).text

    def get_item_phone(self):
        return self.driver.find_element_by_css_selector(self.__ITEM_PHONE).text

    def get_items_count(self):
        return len(self.driver.find_elements_by_css_selector(self.__ITEM_TITLE))

    def set_pagination_count_params(self, count):
        for param in self.driver.find_elements_by_css_selector(self.__PAGINATOR_PARAM):
            if int(param.text) == count:
                param.click()
                return

    def get_pagination_count_current_param(self):
        return int(self.driver.find_element_by_css_selector(self.__PAGINATOR_CURRENT_PARAM).text)


class ShowroomListTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_redirect(self):
        page = ShowroomPage(self.driver)
        page.open()

        showroom_list = page.showroom_list
        item_name = showroom_list.open_first_item()
        item_page_title = showroom_list.get_first_item_page_title()
        self.assertEqual(item_name, item_page_title)

    def test_short_info(self):
        page = ShowroomPage(self.driver)
        page.open()

        showroom_list = page.showroom_list
        self.assertIsNotNone(showroom_list.get_item_address())
        self.assertIsNotNone(showroom_list.get_item_phone())

    def test_pagination(self):
        page = ShowroomPage(self.driver)
        page.open()

        showroom_list = page.showroom_list
        self.assertEqual(showroom_list.get_items_count(), showroom_list.get_pagination_count_current_param())
        count_param = 40
        showroom_list.set_pagination_count_params(count_param)
        self.assertEqual(showroom_list.get_items_count(), count_param)
        count_param = 100
        showroom_list.set_pagination_count_params(count_param)
        self.assertEqual(showroom_list.get_items_count(), count_param)
