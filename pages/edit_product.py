from consts import TEST_PRODUCT
from helpers import Page


class ProductEditPage(Page):
    PATH = "/product/{}/edit".format(TEST_PRODUCT)

    PAGE = ".board"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

    def change_path(self, path):
        self.PATH = "/product/" + path + "/edit"
