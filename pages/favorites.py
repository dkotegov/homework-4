from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.default_page import DefaultPage


class FavouritesPage(DefaultPage):
    PATH = "user/favorite"
    TITLE = ".product-table__title"
    LIKE = ".product-card__like"
    PRODUCT_CARS_TITLE = ".product-card-info__name"
    PRODUCT = ".product-card"

    def get_title(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text

    def remove_like(self, index):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.LIKE)))
        likes = self.driver.find_elements(By.CSS_SELECTOR, self.LIKE)
        likes[index].click()

    def get_product_title(self, index):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.PRODUCT_CARS_TITLE)))
        return self.driver.find_element(By.CSS_SELECTOR, self.PRODUCT_CARS_TITLE).text
    
    def get_products_titles(self):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.PRODUCT_CARS_TITLE)))
        p = self.driver.find_elements(By.CSS_SELECTOR, self.PRODUCT_CARS_TITLE)
        # titles = []
        # for i in range(len(p) - 3):
        #     titles.append(p[i].text)
        return len(p)

    def click_product(self):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.PRODUCT)))
        self.driver.find_element(By.CSS_SELECTOR, self.PRODUCT).click()


