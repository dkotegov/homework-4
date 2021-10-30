from components import ProductCard, Login
from helpers import Page


class UserProductsPage(Page):
    PATH = "user/ad"

    @property
    def product_card(self):
        return ProductCard(self.driver)

    @property
    def login(self):
        return Login(self.driver)
