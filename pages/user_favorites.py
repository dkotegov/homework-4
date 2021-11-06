from helpers import Page
from components import Login, ProductCard


class UserFavoritesPage(Page):
    PATH = "/user/favorite"

    @property
    def login(self):
        return Login(self.driver)

    @property
    def product_card(self):
        return ProductCard(self.driver)
