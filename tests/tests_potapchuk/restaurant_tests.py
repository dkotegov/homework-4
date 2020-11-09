from tests.pages.restaurant_page import RestaurantPage
from tests.tests_potapchuk.base_test import BaseTest


class RestaurantTest(BaseTest):
    def setUp(self):
        super().create_restaurant_with_products(prod_num=2)
        super().setUp(auth='user')

        self.restaurantPage = RestaurantPage(self.driver, self.rest_id)
        self.restaurantPage.open()
        self.restaurantPage.wait_visible()

    def tearDown(self):
        super().clear_restaurant()
        super().tearDown()

    def test_change_guest_quant(self):
        self.assert_guest_quant_num(1)
        guests_add = 3
        for i in range(guests_add):
            self.restaurantPage.inc_guest_num()
            self.assert_guest_quant_num(i + 2)

        for i in range(guests_add):
            self.restaurantPage.dec_guest_num()
            self.assert_guest_quant_num(guests_add - i)

        self.assert_guest_quant_num(1)

    def test_fill_basket(self):
        self.assert_basket_prod_num(0)

        self.restaurantPage.add_product(prod_numeral=0)
        self.assert_basket_prod_num(1)

        self.restaurantPage.add_product_via_basket(prod_numeral=0)
        self.assert_basket_prod_num(2)

        self.restaurantPage.add_product(prod_numeral=1)
        self.assert_basket_prod_num(3)

        self.restaurantPage.del_product(prod_numeral=0)
        self.assert_basket_prod_num(2)

        self.restaurantPage.del_product(prod_numeral=1)
        self.assert_basket_prod_num(1)

        self.restaurantPage.del_product_via_basket(prod_numeral=0)
        self.assert_basket_prod_num(0)

    def assert_basket_prod_num(self, expected_prod_num):
        self.assertEqual(
            expected_prod_num,
            self.restaurantPage.basket_prod_num(),
        )

    def assert_guest_quant_num(self, expected_guest_num):
        self.assertEqual(
            expected_guest_num,
            self.restaurantPage.guest_num()
        )
