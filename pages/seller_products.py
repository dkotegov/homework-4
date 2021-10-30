from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components import ProductCard, Login
from pages.default_page import DefaultPage


class SellerProductsPage(DefaultPage):
    PATH = "user/1/ad"

    TITLE = ".product-table__title"

    @property
    def product_card(self):
        return ProductCard(self.driver)

    @property
    def login(self):
        return Login(self.driver)

    def get_title(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text
#.F.E..........E...EEE.E........E...................E.......E
#.F.F.......E..E...............E...............F....E........
#...........E.......................................E........
