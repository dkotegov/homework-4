import unittest

from tests.default_setup import default_setup
from tests.pages.user.ordering import OrderingPage
from tests.steps.auth_user import auth_setup
from tests.steps.create_basket import create_basket_setup


class MakeOrderFailedTest(unittest.TestCase):
    error_empty_phone = 'Телефон: Поле должно быть заполнено'
    error_incorrect_phone = 'Телефон: Введите настоящий номер телефона'
    phone_empty = ""
    phone_incorrect = "3458"

    restaurant_id = 11
    restaurant_is_no_not_zone = 2

    def setUp(self):
        default_setup(self)
        auth_setup(self)

        self.restaurants_name = create_basket_setup(self, self.restaurant_id)

        self.ordering_page = OrderingPage(self.driver, self.restaurant_id)
        self.ordering_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_make_order_restaurant_is_no_not_zone_failed(self):
        self.restaurants_name = create_basket_setup(self, self.restaurant_is_no_not_zone)
        self.ordering_page = OrderingPage(self.driver, self.restaurant_is_no_not_zone)
        self.ordering_page.open()

        self.ordering_page.click_submit()
        error = self.ordering_page.get_main_error()
        self.assertEqual(error, self.error_address)

    def test_make_order_phone_empty_failed(self):
        self.ordering_page.set_phone(self.phone_empty)
        self.ordering_page.click_submit()
        error = self.ordering_page.get_phone_error()
        self.assertEqual(error, self.error_empty_phone)

    def test_make_order_phone_incorrect_failed(self):
        self.ordering_page.set_phone(self.phone_incorrect)
        self.ordering_page.click_submit()
        error = self.ordering_page.get_phone_error()
        self.assertEqual(error, self.error_incorrect_phone)
