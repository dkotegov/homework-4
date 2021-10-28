from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.default_page import DefaultPage


class HeaderPage(DefaultPage):
    PATH = ""
    LOGO = ".header-left__brand"
    SEARCH = ".header-right__search-button"
    CREATE_BUTTON = ".header-right__create-button"
    AUTH_BUTTON = ".header-right__account"
    ACCOUNT_BUTTON = ".header-right-avatar"
    DROPDOWN = ".header-dropdown-content"
    SETTINGS = "//a[@class=\"header-dropdown-content-item\"]/span[contains(text(),'Настройки')]"
    AD = "//a[@class=\"header-dropdown-content-item\"]/span[contains(text(),'Мои объявления')]"
    CHATS = "//a[@class=\"header-dropdown-content-item\"]/span[contains(text(),'Мои сообщения')]"
    FAVORITES = "//a[@class=\"header-dropdown-content-item\"]/span[contains(text(),'Избранное')]"
    ACHIEVEMENTS = "//a[@class=\"header-dropdown-content-item\"]/span[contains(text(),'Достижения')]"
    REVIEWS = "//a[@class=\"header-dropdown-content-item\"]/span[contains(text(),'Отзывы')]"

    def click_logo(self):
        self.__click_button__(self.LOGO)

    def click_search(self):
        self.__click_button__(self.SEARCH)

    def click_create(self):
        self.__click_button__(self.CREATE_BUTTON)

    def click_auth(self):
        self.__click_button__(self.AUTH_BUTTON)

    def click_dropdown(self):
        self.__click_button__(self.ACCOUNT_BUTTON)

    def is_opened_dropdown(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.DROPDOWN)))
        return True

    def click_settings(self):
        self.__click_button_xpath__(self.SETTINGS)

    def click_ad(self):
        self.__click_button_xpath__(self.AD)

    def click_chats(self):
        self.__click_button_xpath__(self.CHATS)

    def click_favorites(self):
        self.__click_button_xpath__(self.FAVORITES)

    def click_achievements(self):
        self.__click_button_xpath__(self.ACHIEVEMENTS)

    def click_reviews(self):
        self.__click_button_xpath__(self.REVIEWS)
