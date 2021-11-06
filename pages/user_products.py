from helpers import Page
from components import ProductCard, Login, UserSideBar


class UserProductsPage(Page):
    PATH = "/user/ad"

    @property
    def login(self):
        return Login(self.driver)

    @property
    def side_bar(self):
        return UserSideBar(self.driver)

    @property
    def product_card(self):
        return ProductCard(self.driver)
