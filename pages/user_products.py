from helpers import Page
from components import ProductCard, Login, UserSideBar


class UserProductsPage(Page):
    PATH = "/user/ad"

    PAGE = ".product-table"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

    @property
    def login(self):
        return Login(self.driver)

    @property
    def side_bar(self):
        return UserSideBar(self.driver)

    @property
    def product_card(self):
        return ProductCard(self.driver)
