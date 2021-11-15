import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from tests.pages.main import MainPage


class CategoriesAndFiltersTest(unittest.TestCase):
    EXISTING_ADDRESS = 'Россия, Москва, улица Ильинка'
    ADDRESS_WITH_NO_RESTAURANTS = 'Аргентина, Санта Крус'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.main_page = MainPage(self.driver)
        self.main_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_display_restaurants(self):
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)

    def test_display_restaurants_with_address(self):
        self.main_page.address_popup.set_address(self.EXISTING_ADDRESS)
        self.main_page.address_popup.submit()
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)

    def test_display_restaurants_with_one_category(self):
        self.main_page.address_popup.close_popup()
        self.main_page.click_sushi_category()
        self.main_page.wait_restaurants_displayed()
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)

    def test_display_restaurants_with_two_categories(self):
        self.main_page.address_popup.close_popup()
        self.main_page.click_sushi_category()
        self.main_page.click_burgers_category()
        self.main_page.wait_restaurants_displayed()
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)

    def test_display_restaurants_with_time_filter(self):
        self.main_page.address_popup.close_popup()
        self.main_page.choose_time_filter()
        self.main_page.wait_restaurants_displayed()
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)

    def test_display_restaurants_with_receipt_filter(self):
        self.main_page.address_popup.close_popup()
        self.main_page.choose_receipt_filter()
        self.main_page.wait_restaurants_displayed()
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)

    def test_display_restaurants_with_rating_filter(self):
        self.main_page.address_popup.close_popup()
        self.main_page.choose_rating_filter()
        self.main_page.wait_restaurants_displayed()
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)

    def test_display_restaurants_with_all_filters(self):
        self.main_page.address_popup.close_popup()
        self.main_page.choose_time_filter()
        self.main_page.choose_receipt_filter()
        self.main_page.choose_rating_filter()
        self.main_page.wait_restaurants_displayed()
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)

    def test_display_restaurants_with_two_filters_and_categories(self):
        self.main_page.address_popup.close_popup()
        self.main_page.click_sushi_category()
        self.main_page.click_burgers_category()
        self.main_page.choose_receipt_filter()
        self.main_page.choose_rating_filter()
        self.main_page.wait_restaurants_displayed()
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)

    def test_display_restaurants_with_category_filter_and_address(self):
        self.main_page.address_popup.close_popup()
        self.main_page.click_sushi_category()
        self.main_page.choose_receipt_filter()
        self.main_page.navbar.click_address()
        self.main_page.address_popup.set_address(self.EXISTING_ADDRESS)
        self.main_page.address_popup.submit()
        self.main_page.wait_restaurants_displayed()
        is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
        self.assertEqual(is_restaurants_displayed, True)

    # def test_restaurants_not_displayed_by_address_with_no_restaurants(self):
    #     self.main_page.address_popup.close_popup()
    #     self.main_page.navbar.click_address()
    #     self.main_page.address_popup.set_address(self.ADDRESS_WITH_NO_RESTAURANTS)
    #     self.main_page.address_popup.submit()
    #     self.main_page.wait_restaurants_displayed()
    #     is_restaurants_displayed = self.main_page.check_if_restaurants_displayed()
    #     self.assertEqual(is_restaurants_displayed, False)
    #
    # def filters_are_not_reset_after_page_refresh(self):
    #
    # def categories_are_not_reset_after_page_refresh(self):
