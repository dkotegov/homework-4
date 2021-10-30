from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers import Page
from components import ProductCard, Login


class SellerProductsPage(Page):
    PATH = "user/1/ad"

    TITLE = ".product-table__title"

    @property
    def product_card(self):
        return ProductCard(self.driver)

    @property
    def login(self):
        return Login(self.driver)

    def get_title(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.helpers.get_element(self.TITLE).text
