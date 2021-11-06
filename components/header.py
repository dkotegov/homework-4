from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from helpers.component import Component


class Header(Component):
    LOGO = ".header-left__brand__img"
    SEARCH_BUTTON = ".header-right__search-button"
    CREATE_BUTTON = ".header-right__create-button"
    AUTH_BUTTON = ".header-right__account"
    ACCOUNT_BUTTON = ".header-right-avatar"

    DROPDOWN = ".header-dropdown-content"
    DROPDOWN_ITEM = "//a[@class=\"header-dropdown-content-item\"]/span[contains(text(),'{}')]"
    SETTINGS_BUTTON = DROPDOWN_ITEM.format("Настройки")
    PRODUCTS_BUTTON = DROPDOWN_ITEM.format("Мои объявления")
    MESSAGES_BUTTON = DROPDOWN_ITEM.format("Мои сообщения")
    FAVORITES_BUTTON = DROPDOWN_ITEM.format("Избранное")
    ACHIEVEMENTS_BUTTON = DROPDOWN_ITEM.format("Достижения")
    REVIEWS_BUTTON = DROPDOWN_ITEM.format("Отзывы")

    def click_logo(self):
        self.helpers.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.LOGO)))
        self.helpers.click_element(self.LOGO)

    def click_search(self):
        self.helpers.click_element(self.SEARCH_BUTTON)

    def click_create(self):
        self.helpers.click_element(self.CREATE_BUTTON)

    def click_auth(self):
        self.helpers.click_element(self.AUTH_BUTTON)

    def click_dropdown(self):
        self.helpers.click_element(self.ACCOUNT_BUTTON)

    def is_opened_dropdown(self):
        return self.helpers.is_contains(self.DROPDOWN)

    def click_settings(self):
        self.helpers.click_element(self.SETTINGS_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_products(self):
        self.helpers.click_element(self.PRODUCTS_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_messages(self):
        self.helpers.click_element(self.MESSAGES_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_favorites(self):
        self.helpers.click_element(self.FAVORITES_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_achievements(self):
        self.helpers.click_element(self.ACHIEVEMENTS_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_reviews(self):
        self.helpers.click_element(self.REVIEWS_BUTTON, self.helpers.SELECTOR.XPATH)
