import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.car_showrooms.pages.pages import ShowroomPage, Component


class SpecialOffersList(Component):
    __ITEM_TITLE = 'span.offer-mini__title'
    __ITEM_PAGE_TITLE = 'h1.car__title__text'
    __ITEM_YEAR = 'span.offer-mini__info'
    __ITEM_PRICE = 'span.offer-mini__price__box'

    def get_item_titles(self):
        return [item.text for item in self.driver.find_elements_by_css_selector(self.__ITEM_TITLE)]

    def get_item_titles_with_page_titles(self):
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

    def get_items_years(self):
        years = []
        for year in self.driver.find_elements_by_css_selector(self.__ITEM_YEAR):
            years.append(year.text)
        return years

    def get_items_prices(self):
        prices = []
        for price in self.driver.find_elements_by_css_selector(self.__ITEM_PRICE):
            prices.append(price)
        return prices

    def get_items_count(self):
        return len(self.driver.find_elements_by_css_selector(self.__ITEM_TITLE))


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
