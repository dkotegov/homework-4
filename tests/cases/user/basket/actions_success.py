import unittest

from tests.default_setup import default_setup
from tests.pages.user.basket import BasketPage
from tests.steps.auth_user import auth_setup
from tests.steps.create_basket import create_basket_setup


class ActionsBasketSuccessTest(unittest.TestCase):
    restaurant_id = [1, 4]

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.restaurants_name = []

        for basket_id in self.restaurant_id:
            self.restaurants_name.append(create_basket_setup(self, basket_id))

        self.basket_page = BasketPage(self.driver)
        self.basket_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_delete_basket_success(self):
        baskets = self.basket_page.get_all_baskets()
        delete_basket = self.restaurants_name[0]
        delete_id = baskets[delete_basket]
        self.basket_page.delete_basket(delete_id)
        baskets = self.basket_page.get_all_baskets()
        self.assertNotIn(delete_basket, baskets.keys())

    def test_go_to_restaurant(self):
        baskets = self.basket_page.get_all_baskets()
        go_to_basket = self.restaurants_name[0]
        go_to_id = baskets[go_to_basket]
        self.basket_page.go_to_restaurant(go_to_id)
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/store/{}".format(self.restaurant_id[0]))

    def test_go_to_order_page(self):
        baskets = self.basket_page.get_all_baskets()
        go_to_basket = self.restaurants_name[0]
        go_to_id = baskets[go_to_basket]
        self.basket_page.go_to_order_page(go_to_id)
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/basket/{}".format(self.restaurant_id[0]))

    def test_switch_to_table_view(self):
        self.basket_page.switch_to_list()
        self.basket_page.switch_to_table()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/chose/comparison")

    def test_switch_to_list_view(self):
        self.basket_page.switch_to_table()
        self.basket_page.switch_to_list()
        url = self.driver.current_url
        self.assertEqual(url, "https://delivery-borscht.ru/chose/all")
