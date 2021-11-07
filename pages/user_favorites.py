from helpers import Page
from components import Login, ProductCard


class UserFavoritesPage(Page):
    PATH = "/user/favorite"

    PAGE = ".product-table"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

    @property
    def login(self):
        return Login(self.driver)

    @property
    def product_card(self):
        return ProductCard(self.driver)
