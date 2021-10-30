from random import randrange

from helpers import Component, Page
from components import Header, Footer, Theme, Login, ProductCard


class Search(Component):
    SEARCH_INPUT = ".search-line__input"
    SEARCH = ".search-line__button"
    CATEGORY = ".search-category__title"

    def click_search(self):
        self.helpers.click_button(self.SEARCH)

    def input_search_value(self, text):
        self.helpers.input_value(self.SEARCH_INPUT, text)

    def enter_search(self):
        self.helpers.enter(self.SEARCH_INPUT)

    def click_category(self):
        categories = self.helpers.get_elements(self.CATEGORY)
        index = randrange(len(categories))
        category = categories[index].text
        categories[index].click()
        return category


class MainPage(Page):
    PATH = ""

    @property
    def header(self):
        return Header(self.driver)

    @property
    def login(self):
        return Login(self.driver)

    @property
    def search(self):
        return Search(self.driver)

    @property
    def product_card(self):
        return ProductCard(self.driver)

    @property
    def footer(self):
        return Footer(self.driver)

    @property
    def theme(self):
        return Theme(self.driver)
