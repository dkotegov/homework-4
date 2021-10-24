from selenium.webdriver.common.by import By
from pages.default_page import DefaultPage


class AllSellerProducts(DefaultPage):
    PATH = "user/1/ad"
    TITLE = ".product-table__title"

    def get_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text
