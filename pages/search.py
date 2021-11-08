from selenium.webdriver.support.select import Select

from helpers import Page, Component
from components import Login, ProductCard, Header, Footer


class SearchProducts(ProductCard):
    SORT_AMOUNT = "//div[@data-sort=\"{}\"]//span[@class=\"product-card-info__amount\"]"
    SORT_NAME = "//div[@data-sort=\"{}\"]//span[@class=\"product-card-info__name\"]"

    def get_sorted_name_products(self):
        return self.helpers.get_elements(self.SORT_NAME.format("По имени"), self.helpers.SELECTOR.XPATH)

    def get_sorted_amount_up_products(self):
        return self.helpers.get_elements(self.SORT_AMOUNT.format("По возрастанию цены"), self.helpers.SELECTOR.XPATH)

    def get_sorted_amount_down_products(self):
        return self.helpers.get_elements(self.SORT_AMOUNT.format("По убыванию цены"), self.helpers.SELECTOR.XPATH)


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


class SearchSort(Component):
    SORT = ".search-items__sort"

    def change_sort_name(self):
        self.__change_sort__('По имени')

    def change_sort_amount_down(self):
        self.__change_sort__('По убыванию цены')

    def change_sort_amount_up(self):
        self.__change_sort__('По возрастанию цены')

    def __change_sort__(self, param):
        sort = Select(self.helpers.get_element(self.SORT))
        sort.select_by_visible_text(param)


class SearchPage(Page):
    PATH = "/search"

    PAGE = ".search-filter"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

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

    @property
    def search_sort(self):
        return SearchSort(self.driver)
