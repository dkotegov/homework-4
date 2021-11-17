import unittest

from tests.default_setup import default_setup
from tests.pages.user.ordering import OrderingPage
from tests.steps.auth_user import auth_setup
from tests.steps.create_basket import create_basket_setup


class MakeOrderSuccessTest(unittest.TestCase):
    new_phone = "9197666111"
    comment = "comment"
    comment_empty = ""
    comment_quotes = "'comment'"
    restaurant_id = 11

    def setUp(self):
        default_setup(self)
        auth_setup(self)

        self.restaurants_name = create_basket_setup(self, self.restaurant_id)

        self.ordering_page = OrderingPage(self.driver, self.restaurant_id)
        self.ordering_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_make_order_success(self):
        self.ordering_page.click_submit()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/profile/orders")

    def test_make_order_updating_phone_success(self):
        self.ordering_page.set_phone(self.new_phone)
        self.ordering_page.click_submit()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/profile/orders")

    def test_make_order_with_comment_success(self):
        self.ordering_page.set_comment(self.comment)
        self.ordering_page.click_submit()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/profile/orders")

    def test_make_order_with_comment_empty_success(self):
        self.ordering_page.set_comment(self.comment_empty)
        self.ordering_page.click_submit()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/profile/orders")

    def test_make_order_with_comment_quotes_success(self):
        self.ordering_page.set_comment(self.comment_quotes)
        self.ordering_page.click_submit()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/profile/orders")
