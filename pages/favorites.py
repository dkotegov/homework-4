from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helpers import Page
from components import Login, ProductCard


class FavouritesPage(Page):
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

    def get_title(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.helpers.get_element(self.TITLE).text

    def get_product_title(self, index):
        self.helpers.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.PRODUCT_CARS_TITLE)))
        return self.helpers.get_element(self.PRODUCT_CARS_TITLE).text
    
    def count_products(self):
        self.helpers.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.PRODUCT_CARS_TITLE)))
        p = self.helpers.get_elements(self.PRODUCT_CARS_TITLE)
        return len(p)


