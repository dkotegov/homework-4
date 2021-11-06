from selenium.webdriver.common.by import By

from helpers.component import Component


class ProductCard(Component):
    PRODUCT_CARD = '.product-card'
    PRODUCT_CARD_ID = '//div[@data-card-id={}]'
    INFO = '.product-card-info'
    LIKE = ".product-card__like"
    LIKED = "product-card__like_liked"

    def count_products(self):
        return len(self.helpers.get_elements(self.PRODUCT_CARD))

    def get_product_id(self):
        element = self.helpers.get_element(self.PRODUCT_CARD)
        return element.get_attribute("data-card-id")

    def click_product(self, product_id):
        element = self.helpers.get_element(self.PRODUCT_CARD_ID.format(product_id), self.helpers.SELECTOR.XPATH)
        element.find_element(By.CSS_SELECTOR, self.INFO).click()

    def click_like_product(self, product_id):
        element = self.helpers.get_element(self.PRODUCT_CARD_ID.format(product_id), self.helpers.SELECTOR.XPATH)
        element.find_element(By.CSS_SELECTOR, self.LIKE).click()

    def is_product_liked(self, product_id):
        element = self.helpers.get_element(self.PRODUCT_CARD_ID.format(product_id), self.helpers.SELECTOR.XPATH)
        like = element.find_element(By.CSS_SELECTOR, self.LIKE)
        return self.helpers.is_element_contains_class(like, self.LIKED)
