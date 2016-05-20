import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.car_showrooms.pages.pages import ShowroomPage, Component


class ShowroomList(Component):
    __ITEM = '//div[contains(@class, "dealer-card_lst") or contains(@class, "dealer-card clear")]'
    __ITEM_TITLE = 'div.dealer-card__title a'
    __ITEM_PAGE_TITLE = 'span.bread__curr'
    __ITEM_ADDRESS = 'div.dealer-card__adress'
    __ITEM_PHONE = 'div.dealer-card__phone'
    __PAGINATOR_CURRENT_PARAM = "a.pager__pin.pager__pin_perpage.pager__pin_on"
    __PAGINATOR_PARAM = "a.pager__pin.pager__pin_perpage"
    __DEALER_MODEL_ICON = '//img[@alt and @title and @class="dealer-card__aside__item"]'
    __DEALER_MODEL_ICON_FOR_MODEL_FORMAT = '//img[@alt="{0}" and @title="{0}" and @class="dealer-card__aside__item"]'
    __DEALER_CARD_METRO_STATION = '//span[@class="dealer-card__metro__item"]'
    __EMPTY_LIST_MESSAGE = '//div[@class="empty"]'

    def get_item_titles(self):
        item_titles = []
        item_pages_title = []

        items_count = self.get_items_count()
        items_ids = [0, items_count/2, items_count - 1]
        for item_id in items_ids:
            item = self.driver.find_elements_by_css_selector(self.__ITEM_TITLE)[item_id]

            item_titles.append(item.text)
            item.click()
            item_pages_title.append(self.get_item_page_title())
            self.driver.back()

        return item_titles, item_pages_title

    def get_item_page_title(self):
        return self.driver.find_element_by_css_selector(self.__ITEM_PAGE_TITLE).text

    def get_items_addresses(self):
        addresses = []
        for address in self.driver.find_elements_by_css_selector(self.__ITEM_ADDRESS):
            addresses.append(address.text)
        return addresses

    def get_items_phones(self):
        phones = []
        for phone in self.driver.find_elements_by_css_selector(self.__ITEM_PHONE):
            phones.append(phone.text)
        return phones

    def get_items_count(self):
        return len(self.driver.find_elements_by_xpath(self.__ITEM))

    def set_pagination_count_params(self, count):
        for param in self.driver.find_elements_by_css_selector(self.__PAGINATOR_PARAM):
            if int(param.text) == count:
                param.click()
                return

    def get_pagination_count_current_param(self):
        return int(self.driver.find_element_by_css_selector(self.__PAGINATOR_CURRENT_PARAM).text)

    def get_items_official_dealers_by_model(self, model):
        return self.driver.find_elements_by_xpath(self.__DEALER_MODEL_ICON_FOR_MODEL_FORMAT.format(model))

    def get_items_metro_stations(self):
        return [item.text for item in self.driver.find_elements_by_xpath(self.__DEALER_CARD_METRO_STATION)]

    def is_list_empty(self):
        try:
            empty_message = self.driver.find_elements_by_xpath(self.__EMPTY_LIST_MESSAGE)
            return True
        except Exception:
            return False

    def get_items_official_dealers(self):
        official_items = []
        items = self.driver.find_elements_by_xpath(self.__ITEM)
        for item in items:
            dealer_model_icons = []
            try:
                dealer_model_icons = item.find_elements_by_xpath(self.__DEALER_MODEL_ICON)
            except Exception:
                pass

            if len(dealer_model_icons) > 0:
                official_items.append(item)

        return official_items


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
        item_titles, item_page_title = showroom_list.get_item_titles()
        for i in range(0, len(item_titles)):
            self.assertEqual(item_titles[i], item_page_title[i])

    def test_short_info(self):
        page = ShowroomPage(self.driver)
        page.open()

        showroom_list = page.showroom_list

        addresses = showroom_list.get_items_addresses()
        phones = showroom_list.get_items_phones()

        self.assertEqual(len(addresses), showroom_list.get_items_count())
        self.assertEqual(len(phones), showroom_list.get_items_count())

        items_count = showroom_list.get_items_count()
        items_ids = [0, items_count/2 - 4, items_count/2, items_count/2 + 4, items_count - 1]
        for item_id in items_ids:
            address = addresses[item_id]
            self.assertIsNotNone(address)

            phone = phones[item_id]
            self.assertIsNotNone(phone)

    def test_pagination(self):
        page = ShowroomPage(self.driver)
        page.open()

        count_params = [20, 40, 100]
        showroom_list = page.showroom_list
        self.assertEqual(showroom_list.get_items_count(), showroom_list.get_pagination_count_current_param())

        for count_param in count_params:
            showroom_list.set_pagination_count_params(count_param)
            self.assertEqual(showroom_list.get_items_count(), count_param)
