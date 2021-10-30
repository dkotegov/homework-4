from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.default_page import DefaultPage


class ProductEditPage(DefaultPage):
    PATH = "product/198/edit"

    def change_path(self, path):
        self.PATH = "product/" + path + "/edit"
