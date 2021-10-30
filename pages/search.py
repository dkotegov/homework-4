import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from helpers import Page
from components import Login, ProductCard


class SearchPage(Page):
    PATH = "search"
    FROM_A = ".search-filter-amount__from"
    TO_A = ".search-filter-amount__to"
    PRODUCTS = ".product-card"
    PRODUCTS_NAME = ".product-card-info__name"
    PRODUCTS_AMOUNT = ".product-card-info__amount"
    SORT = ".search-items__sort"

    elements = []

    @property
    def login(self):
        return Login(self.driver)

    @property
    def product_card(self):
        return ProductCard(self.driver)

    def change_path(self, path):
        self.PATH = "search/" + path

    def clear_amount(self):
        self.helpers.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.FROM_A)))
        self.helpers.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.TO_A)))
        from_a = self.helpers.get_element(self.FROM_A)
        to_a = self.helpers.get_element(self.TO_A)
        from_a.clear()
        to_a.clear()

    def enter_amount(self, text):
        self.helpers.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.FROM_A)))
        self.helpers.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.TO_A)))
        from_a = self.helpers.get_element(self.FROM_A)
        from_a.send_keys(text)
        to_a = self.helpers.get_element(self.TO_A)
        to_a.send_keys(text)
        return from_a.get_attribute('value'), to_a.get_attribute('value')

    def get_all_name_products(self):
        products = []
        while self.elements == self.helpers.get_elements(self.PRODUCTS_NAME):
            time.sleep(0.06)
            products = self.helpers.get_elements(self.PRODUCTS_NAME)
        return products

    def get_all_amount_products(self):
        products = []
        while self.elements == self.helpers.get_elements(self.PRODUCTS_AMOUNT):
            time.sleep(0.06)
            products = self.helpers.get_elements(self.PRODUCTS_AMOUNT)
        return products

    def change_sort_name(self):
        self.elements = self.helpers.get_elements(self.PRODUCTS_NAME)
        self.__change_sort__('По имени')

    def change_sort_amount_down(self):
        self.elements = self.helpers.get_elements(self.PRODUCTS_AMOUNT)
        self.__change_sort__('По убыванию цены')

    def change_sort_amount_up(self):
        self.elements = self.helpers.get_elements(self.PRODUCTS_AMOUNT)
        self.__change_sort__('По возрастанию цены')

    def __change_sort__(self, param):
        self.helpers.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.SORT)))
        sort = Select(self.helpers.get_element(self.SORT))
        sort.select_by_visible_text(param)
