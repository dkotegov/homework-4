from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helpers import Page
from components import Login, ProductCard, SideBar


class FavoritesPage(Page):
    PATH = "user/favorite"
    TITLE = ".product-table__title"
    LIKE = ".product-card__like"
    PRODUCT_CARS_TITLE = ".product-card-info__name"
    PRODUCT = ".product-card"

    @property
    def login(self):
        return Login(self.driver)

    @property
    def product_card(self):
        return ProductCard(self.driver)

    @property
    def side_bar(self):
        return SideBar(self.driver)
    
    def count_products(self):
        p = self.helpers.get_elements(self.PRODUCT_CARS_TITLE)
        return len(p)


