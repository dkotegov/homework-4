import time
from random import randrange
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.default_page import DefaultPage


class SearchPage(DefaultPage):
    PATH = "search"
    FROM_A = ".search-filter-amount__from"
    TO_A = ".search-filter-amount__to"
    PRODUCTS = ".product-card"

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