from random import randrange
from selenium.webdriver.common.by import By
from pages.default_page import DefaultPage
from selenium.webdriver.support import expected_conditions as EC


class AllSellerProductsPage(DefaultPage):
    PATH = "user/1/ad"
    TITLE = ".product-table__title"
    PRODUCTS = ".product-card"
    LIKE = ".product-card__like"

    def get_title(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text

    def clickProduct(self):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.PRODUCTS)))
        products = self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCTS)
        products[randrange(len(products))].click()

    def likeProduct(self):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.LIKE)))
        likes = self.driver.find_elements(By.CSS_SELECTOR, self.LIKE)
        likes[randrange(len(likes))].click()
