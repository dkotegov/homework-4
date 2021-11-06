from random import randrange

from helpers.component import Component


class ProductCard(Component):
    PRODUCT_CARD = ".product-card"
    PRODUCT_CARD_ID = "//div[@data-card-id={}]"
    INFO = "{}//div[@class=\"product-card-info\"]".format(PRODUCT_CARD_ID)
    LIKE = "{}//*[@class=\"product-card__like\"]".format(PRODUCT_CARD_ID)
    LIKED = "product-card__like_liked"

    def count_products(self):
        return len(self.helpers.get_elements(self.PRODUCT_CARD))

    def get_product_id(self):
        elements = self.helpers.get_elements(self.PRODUCT_CARD)
        index = randrange(len(elements)) - 1
        return elements[index].get_attribute("data-card-id")

    def click_product(self, product_id):
        self.helpers.click_element(self.INFO.format(product_id), self.helpers.SELECTOR.XPATH)

    def click_like_product(self, product_id):
        self.helpers.click_element(self.LIKE.format(product_id), self.helpers.SELECTOR.XPATH)

    def is_product_liked(self, product_id):
        return self.helpers.is_contains(self.LIKE.format(product_id), self.LIKED, self.helpers.SELECTOR.XPATH)
