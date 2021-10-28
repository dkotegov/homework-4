from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.default_page import DefaultPage


class MainPage(DefaultPage):
    PATH = ""
    SEARCH_INPUT = ".search-line__input"
    SEARCH = ".search-line__button"

    def click_search(self):
        self.__click_button__(self.SEARCH)

    def input_search_value(self, text):
        search_input = self.driver.find_element(By.CSS_SELECTOR, self.SEARCH_INPUT)
        search_input.send_keys(text)

    def enter_search(self):
        search_input = self.driver.find_element(By.CSS_SELECTOR, self.SEARCH_INPUT)
        search_input.send_keys(Keys.ENTER)
