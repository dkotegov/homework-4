from random import randrange

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from helpers.component import Component


class ProductCard(Component):
    PRODUCT_CARD = ".product-card"
    PRODUCT_CARD_ID = "//div[@data-card-id={}]"
    INFO = "{}//div[@class=\"product-card-info\"]".format(PRODUCT_CARD_ID)
    LIKE = "{}//*[contains(@class, \"product-card__like\")]".format(PRODUCT_CARD_ID)
    NOT_LIKED_ELEMENT = "{}//*[@class=\"product-card__like\"]".format(PRODUCT_CARD_ID)
    LIKED_ELEMENT = "{}//*[@class=\"product-card__like product-card__like_liked\"]".format(PRODUCT_CARD_ID)
    LIKED_CLASS = "product-card__like_liked"

    def count_products(self):
        return len(self.helpers.get_elements(self.PRODUCT_CARD))

    def get_product_id(self):
        elements = self.helpers.get_elements(self.PRODUCT_CARD)
        index = randrange(len(elements)) - 1
        return elements[index].get_attribute("data-card-id")

    def click_product(self, product_id):
        self.helpers.click_element(self.INFO.format(product_id), self.helpers.SELECTOR.XPATH)

    def click_like_product(self, product_id):
        self.helpers.wait(until=EC.element_to_be_clickable((By.XPATH, self.LIKE.format(product_id))))
        self.helpers.click_element(self.LIKE.format(product_id), self.helpers.SELECTOR.XPATH)

    def is_product_liked(self, product_id):
        return self.helpers.is_contains_class(self.LIKE.format(product_id), self.LIKED_CLASS, self.helpers.SELECTOR.XPATH)

    def wait_liked(self, product_id):
        self.helpers.wait(until=EC.element_to_be_clickable((By.XPATH, self.LIKED_ELEMENT.format(product_id))))

    def wait_not_liked(self, product_id):
        self.helpers.wait(until=EC.element_to_be_clickable((By.XPATH, self.NOT_LIKED_ELEMENT.format(product_id))))

    def wait_product_disappeared(self, product_id):
        self.helpers.wait(until=EC.invisibility_of_element_located((By.XPATH, self.PRODUCT_CARD_ID.format(product_id))))
