from helpers import Page


class ProductEditPage(Page):
    PATH = "/product/198/edit"

    def change_path(self, path):
        self.PATH = "/product/" + path + "/edit"
