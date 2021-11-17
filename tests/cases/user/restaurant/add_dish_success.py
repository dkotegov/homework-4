import unittest

from tests.default_setup import default_setup
from tests.pages.user.restaurant import RestaurantPage


class AddDishToBasketSuccessTest(unittest.TestCase):
    def setUp(self):
        default_setup(self)
        self.restaurant_page = RestaurantPage(self.driver, 1)
        self.restaurant_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_add_dish(self):
        self.assertLess(0, self.restaurant_page.get_number_dish_in_menu())
        self.restaurant_page.add_to_basket_dish(0)
        basket = self.restaurant_page.get_basket_dishes()
        self.assertEqual(1, len(basket))
        self.assertEqual(self.restaurant_page.get_name_dish(0), basket[0]['name'])

    def test_increase_dish(self):
        self.assertLess(0, self.restaurant_page.get_number_dish_in_menu())
        self.restaurant_page.add_to_basket_dish(0)
        self.restaurant_page.increase_dish(0)
        basket = self.restaurant_page.get_basket_dishes()
        self.assertEqual(1, len(basket))
        self.assertEqual('2', self.restaurant_page.get_count_dish(0))
        self.assertEqual('2', basket[0]['count'])

    def test_decrease_dish(self):
        self.assertLess(0, self.restaurant_page.get_number_dish_in_menu())
        self.restaurant_page.add_to_basket_dish(0)
        self.restaurant_page.increase_dish(0)
        self.restaurant_page.decrease_dish(0)
        basket = self.restaurant_page.get_basket_dishes()
        self.assertEqual(1, len(basket))
        self.assertEqual('1', self.restaurant_page.get_count_dish(0))
        self.assertEqual('1', basket[0]['count'])

    def test_add_more_dish(self):
        self.assertLess(2, self.restaurant_page.get_number_dish_in_menu())
        self.restaurant_page.add_to_basket_dish(0)
        self.restaurant_page.add_to_basket_dish(1)
        self.restaurant_page.add_to_basket_dish(2)
        basket = self.restaurant_page.get_basket_dishes()
        self.assertEqual(3, len(basket))
