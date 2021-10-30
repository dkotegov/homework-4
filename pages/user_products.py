from helpers import Page
from components import ProductCard, Login, Footer


class UserProductsPage(Page):
    PATH = "user/ad"

    @property
    def footer(self):
        return Footer(self.driver)

    @property
    def login(self):
        return Login(self.driver)

    @property
    def product_card(self):
        return ProductCard(self.driver)
