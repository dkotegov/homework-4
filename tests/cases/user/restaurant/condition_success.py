import unittest

from tests.default_setup import default_setup
from tests.pages.user.restaurant import RestaurantPage
from tests.steps.auth_user import auth_setup


class ConditionSuccessTest(unittest.TestCase):
    restaurant_number = 1

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.restaurant_page = RestaurantPage(self.driver, self.restaurant_number)
        self.restaurant_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_save_on_refresh(self):
        self.assertLess(2, self.restaurant_page.get_number_dish_in_menu())
        self.restaurant_page.add_to_basket_dish(0)
        self.restaurant_page.add_to_basket_dish(1)
        self.restaurant_page.add_to_basket_dish(2)
        self.restaurant_page.refresh_page()
        basket = self.restaurant_page.get_basket_dishes()
        self.assertEqual(3, len(basket))

        self.restaurant_page.decrease_dish(0)
        self.restaurant_page.decrease_dish(1)
        self.restaurant_page.decrease_dish(2)

    def test_go_to_checkout(self):
        self.restaurant_page.go_to_checkout()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/basket/" + str(self.restaurant_number))

    def test_go_to_comparison(self):
        self.restaurant_page.go_to_comparison()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/chose/comparison")
