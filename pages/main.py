from random import randrange

from pages.default_page import DefaultPage


class MainPage(DefaultPage):
    PATH = ""

    SEARCH_INPUT = ".search-line__input"
    SEARCH = ".search-line__button"
    CATEGORY = ".search-category__title"
    PRODUCTS = ".product-card"
    PRODUCT_LIKE = ".product-card__like"

    def click_search(self):
        self.__click_button__(self.SEARCH)

    def input_search_value(self, text):
        self.__input_value__(self.SEARCH_INPUT, text)

    def enter_search(self):
        self.__enter__(self.SEARCH_INPUT)

    def click_category(self):
        categories = self.__get_elements__(self.CATEGORY)
        index = randrange(len(categories))
        category = categories[index].text
        categories[index].click()
        return category
