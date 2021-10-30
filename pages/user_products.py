from components import ProductCard, Login
from pages.default_page import DefaultPage


class UserProductsPage(DefaultPage):
    PATH = "user/ad"

    @property
    def product_card(self):
        return ProductCard(self.driver)

    @property
    def login(self):
        return Login(self.driver)
