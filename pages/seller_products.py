from consts import SELLER_USER
from helpers import Page
from components import ProductCard, Login, SellerSideBar


class SellerProductsPage(Page):
    PATH = "/user/{}/ad".format(SELLER_USER)
    TITLE = ".product-table__title"

    PAGE = ".product-table"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

    def change_path(self, path):
        self.PATH = "/user/" + path + "/ad"

    def page_exist(self):
        return self.helpers.get_element(self.TITLE) is not None

    @property
    def product_card(self):
        return ProductCard(self.driver)

    @property
    def login(self):
        return Login(self.driver)

    @property
    def side_bar(self):
        return SellerSideBar(self.driver)
