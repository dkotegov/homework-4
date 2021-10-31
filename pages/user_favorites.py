from helpers import Page
from components import Login, ProductCard


class FavoritesProducts(ProductCard):
    PRODUCT_CARD_TITLE = ".product-card-info__name"

    def count_products(self):
        return len(self.helpers.get_elements(self.PRODUCT_CARD_TITLE))


class UserFavoritesPage(Page):
    PATH = "user/favorite"

    @property
    def login(self):
        return Login(self.driver)

    @property
    def favorite_products(self):
        return FavoritesProducts(self.driver)
