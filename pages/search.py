import time
from random import randrange
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.default_page import DefaultPage


class SearchPage(DefaultPage):
    PATH = "search"
    FROM_A = ".search-filter-amount__from"
    TO_A = ".search-filter-amount__to"
    PRODUCTS = ".product-card"
    PRODUCTS_NAME = ".product-card-info__name"
    PRODUCTS_AMOUNT = ".product-card-info__amount"
    SORT = ".search-items__sort"

    elements = []

    def clearAmount(self):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.FROM_A)))
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.TO_A)))
        from_a = self.driver.find_element(By.CSS_SELECTOR, self.FROM_A)
        to_a = self.driver.find_element(By.CSS_SELECTOR, self.TO_A)
        from_a.clear()
        to_a.clear()

    def enterAmount(self, text):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.FROM_A)))
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.TO_A)))
        from_a = self.driver.find_element(By.CSS_SELECTOR, self.FROM_A)
        from_a.send_keys(text)
        to_a = self.driver.find_element(By.CSS_SELECTOR, self.TO_A)
        to_a.send_keys(text)
        return from_a.get_attribute('value'), to_a.get_attribute('value')

    def clickProduct(self):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.PRODUCTS)))
        products = self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCTS)
        products[randrange(len(products))].click()

    def getAllNameProducts(self):
        products = []
        while self.elements == self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCTS_NAME):
            time.sleep(0.05)
            products = self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCTS_NAME)
        return products

    def getAllAmountProducts(self):
        products = []
        while self.elements == self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCTS_AMOUNT):
            time.sleep(0.05)
            products = self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCTS_AMOUNT)
        return products

    def changeSortName(self):
        self.elements = self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCTS_NAME)
        self.__changeSort('По имени')

    def changeSortAmountDown(self):
        self.elements = self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCTS_AMOUNT)
        self.__changeSort('По убыванию цены')

    def changeSortAmountUp(self):
        self.elements = self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCTS_AMOUNT)
        self.__changeSort('По возрастанию цены')

    def __changeSort(self, param):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.SORT)))
        sort = Select(self.driver.find_element(By.CSS_SELECTOR, self.SORT))
        sort.select_by_visible_text(param)
