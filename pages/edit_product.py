from consts import TEST_PRODUCT
from helpers import Page


class ProductEditPage(Page):
    PATH = "/product/{}/edit".format(TEST_PRODUCT)

    def change_path(self, path):
        self.PATH = "/product/" + path + "/edit"
