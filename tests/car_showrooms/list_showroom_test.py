import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.car_showrooms.pages.pages import ShowroomPage


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
        items_ids = [0, items_count / 2 - 4, items_count / 2, items_count / 2 + 4, items_count - 1]
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
