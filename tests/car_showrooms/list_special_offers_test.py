import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.car_showrooms.pages.pages import ShowroomPage


class SpecialOffersListTest(unittest.TestCase):
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

        special_offers_list = page.special_offers_list
        item_titles, item_page_title = special_offers_list.get_item_titles_with_page_titles()
        for i in range(0, len(item_titles)):
            self.assertTrue(item_page_title[i].startswith(item_titles[i]))

    def test_short_info(self):
        page = ShowroomPage(self.driver)
        page.open()

        special_offers_list = page.special_offers_list

        years = special_offers_list.get_items_years()
        prices = special_offers_list.get_items_prices()

        self.assertEqual(len(years), special_offers_list.get_items_count())
        self.assertEqual(len(prices), special_offers_list.get_items_count())

        items_count = special_offers_list.get_items_count()
        items_ids = [0, items_count/2, items_count - 1]
        for item_id in items_ids:
            year = years[item_id]
            self.assertIsNotNone(year)

            price = prices[item_id]
            self.assertIsNotNone(price)
