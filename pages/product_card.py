from random import randrange

from pages.default_page import DefaultPage


class ProductCard(DefaultPage):
    PRODUCTS = ".product-card"
    PRODUCT_LIKE = ".product-card__like"
    PRODUCT_LIKED = "product-card__like_liked"
    LIKED = ".product-card__like_liked"

    def click_product(self):
        products = self.__get_elements__(self.PRODUCTS)
        index = randrange(len(products))
        product_id = products[index].get_attribute("data-card-id")
        products[index].click()
        return product_id

    def like_product(self):
        products = self.__get_elements__(self.PRODUCT_LIKE)
        index = randrange(10)
        products[index].click()
        return index

    def remove_like_product(self, index):
        products = self.__get_elements__(self.PRODUCT_LIKE)
        products[index].click()
        return index

    def check_like_product(self, index):
        products = self.__get_elements__(self.PRODUCT_LIKE)
        liked = products[index]
        return self.__contains_class__(liked, self.PRODUCT_LIKED)

    def check_remove_like_product(self, index):
        products = self.__get_elements__(self.PRODUCT_LIKE)
        liked = products[index]
        while self.__contains_class__(liked, self.PRODUCT_LIKED):
            continue
        return False
