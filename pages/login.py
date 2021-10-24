from selenium.webdriver.common.by import By
from pages.default_page import DefaultPage


class LoginPage(DefaultPage):
    PATH = ""
    TITLE = ".auth-content-inner__title"

    def get_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text
