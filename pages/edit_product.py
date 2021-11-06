from consts import DEFAULT_PRODUCT
from helpers import Page


class ProductEditPage(Page):
    PATH = "/product/{}/edit".format(DEFAULT_PRODUCT)

    def change_path(self, path):
        self.PATH = "/product/" + path + "/edit"
