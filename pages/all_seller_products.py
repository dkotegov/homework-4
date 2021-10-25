import time
from random import randrange
from selenium.webdriver.common.by import By
from pages.default_page import DefaultPage
from selenium.webdriver.support import expected_conditions as EC


class AllSellerProductsPage(DefaultPage):
    PATH = "user/1/ad"
    TITLE = ".product-table__title"
    PRODUCTS = ".product-card"
    LIKE = ".product-card__like"
    LIKED_CLASS = "product-card__like product-card__like_liked"
    LIKED = ".product-card__like_liked"

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
        index = randrange(5)
        likes[index].click()
        return index

    def removeLikeProduct(self, index):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.LIKE)))
        likes = self.driver.find_elements(By.CSS_SELECTOR, self.LIKE)
        likes[index].click()

    def checkLikeProduct(self, index):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.LIKED)))
        likes = self.driver.find_elements(By.CSS_SELECTOR, self.LIKE)
        liked = likes[index]
        if liked.get_attribute("class") == self.LIKED_CLASS:
            return True
        else:
            return False

    def checkRemovedLikeProduct(self, index):
        likes = self.driver.find_elements(By.CSS_SELECTOR, self.LIKE)
        liked = likes[index]
        while liked.get_attribute("class") == self.LIKED_CLASS:
            continue
        return False
