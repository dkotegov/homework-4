from consts import TEST_PRODUCT
from helpers import Page


class ProductEditPage(Page):
    PATH = "/product/{}/edit".format(TEST_PRODUCT)
    TITLE = ".reg-panel-title__product-name"

    def change_path(self, path):
        self.PATH = "/product/" + path + "/edit"

    def page_exist(self):
        return self.helpers.get_element(self.TITLE) is not None
