import time

from selenium.webdriver.support.select import Select

from helpers import Page, Component
from components import Login, ProductCard, Header, Footer


class SearchProducts(ProductCard):
    PRODUCTS = ".product-card"
    PRODUCTS_NAME = ".product-card-info__name"
    PRODUCTS_AMOUNT = ".product-card-info__amount"
    elements = []

    def save_products_amount(self):
        self.elements = self.helpers.get_elements(self.PRODUCTS_AMOUNT)

    def save_products_name(self):
        self.elements = self.helpers.get_elements(self.PRODUCTS_NAME)

    def get_all_name_products(self):
        products = []
        while self.elements == self.helpers.get_elements(self.PRODUCTS_NAME) or len(products) == 0:
            time.sleep(0.06)  # Самодельный wait. Ждём пока лента обновится
            products = self.helpers.get_elements(self.PRODUCTS_NAME)
        return products

    def get_all_amount_products(self):
        products = []
        while self.elements == self.helpers.get_elements(self.PRODUCTS_AMOUNT) or len(products) == 0:
            time.sleep(0.06)  # Самодельный wait. Ждём пока лента обновится
            products = self.helpers.get_elements(self.PRODUCTS_AMOUNT)
        return products


class SearchSettings(Component):
    FROM_A = ".search-filter-amount__from"
    TO_A = ".search-filter-amount__to"

    def clear_amount(self):
        self.helpers.clear_input(self.FROM_A)
        self.helpers.clear_input(self.TO_A)

    def enter_amount(self, first_value, second_value):
        self.helpers.input_value(self.FROM_A, first_value)
        self.helpers.input_value(self.TO_A, second_value)

    def get_amounts(self):
        from_a = self.helpers.get_element(self.FROM_A)
        to_a = self.helpers.get_element(self.TO_A)
        return from_a.get_attribute('value'), to_a.get_attribute('value')


class SearchPage(Page):
    PATH = "/search"

    SORT = ".search-items__sort"

    def change_path(self, path):
        self.PATH = "/search/" + path

    @property
    def header(self):
        return Header(self.driver)

    @property
    def footer(self):
        return Footer(self.driver)

    @property
    def login(self):
        return Login(self.driver)

    @property
    def search_products(self):
        return SearchProducts(self.driver)

    @property
    def search_settings(self):
        return SearchSettings(self.driver)

    def change_sort_name(self):
        self.search_products.save_products_name()
        self.__change_sort__('По имени')

    def change_sort_amount_down(self):
        self.search_products.save_products_amount()
        self.__change_sort__('По убыванию цены')

    def change_sort_amount_up(self):
        self.search_products.save_products_amount()
        self.__change_sort__('По возрастанию цены')

    def __change_sort__(self, param):
        sort = Select(self.helpers.get_element(self.SORT))
        sort.select_by_visible_text(param)
