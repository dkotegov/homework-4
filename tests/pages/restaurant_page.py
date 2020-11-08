from tests.components.basket import Basket
from tests.components.header import Header
from tests.components.product_list import ProductList
from tests.components.restaurant_banner import RestaurantBanner
from tests.pages.page import Page


class RestaurantPage(Page):
    def __init__(self, driver, rest_id=-1, product_page=1):
        super().__init__(driver)
        self.rest_id = rest_id
        self.prod_page = product_page
        self.PATH = 'restaurants/%d/products/%d' % (rest_id, product_page)

        self.header = Header(self.driver)
        self.rest_banner = RestaurantBanner(self.driver)
        self.rest_products = ProductList(self.driver)
        self.basket = Basket(self.driver)

    def wait_visible(self):
        self.rest_banner.wait_visible() and \
            self.header.wait_visible() and \
            self.rest_products.wait_visible()

    def inc_guest_num(self):
        self.show_basket()
        self.basket.inc_guest_num()

    def dec_guest_num(self):
        self.show_basket()
        self.basket.dec_guest_num()

    def add_product(self, prod_numeral):
        self.rest_products.add_product(prod_numeral)

    def del_product(self, prod_numeral):
        self.rest_products.del_product(prod_numeral)

    def basket_prod_num(self):
        self.show_basket()
        return self.basket.prod_num()

    def guest_num(self):
        self.show_basket()
        return self.basket.guest_num()

    def add_product_via_basket(self, prod_numeral):
        self.show_basket()
        self.basket.add_product(prod_numeral)

    def show_basket(self):
        if not self.basket.is_shown():
            self.header.show_basket()
            self.basket.wait_visible()

    def del_product_via_basket(self, prod_numeral):
        self.show_basket()
        self.basket.del_product(prod_numeral)
