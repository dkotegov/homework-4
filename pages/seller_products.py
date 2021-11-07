from consts import SELLER_USER
from helpers import Page
from components import ProductCard, Login, SellerSideBar


class SellerProductsPage(Page):
    PATH = "/user/{}/ad".format(SELLER_USER)

    def change_path(self, path):
        self.PATH = "/user/" + path + "/ad"

    @property
    def product_card(self):
        return ProductCard(self.driver)

    @property
    def login(self):
        return Login(self.driver)

    @property
    def side_bar(self):
        return SellerSideBar(self.driver)
