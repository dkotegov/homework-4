
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.default_page import DefaultPage


class SideBarPage(DefaultPage):
    MY_SETTINGS = "#profile-menu-settings"
    MY_PRODUCTS = "#profile-menu-posts"
    MY_MESSAGES = "#profile-menu-messages"
    MY_FAVORITES = "#profile-menu-favorites"
    MY_ACHIVEMENTS = "#profile-menu-achievements"
    MY_COMMENTS = "#profile-menu-comments"
    MY_REVIEW_AWAITS = "#profile-menu-review-await"

    def click_my_settings(self):
        self.__click_button__(self.MY_SETTINGS)

    def click_my_products(self):
        self.__click_button__(self.MY_PRODUCTS)

    def click_my_messages(self):
        self.__click_button__(self.MY_MESSAGES)

    def click_my_favorites(self):
        self.__click_button__(self.MY_FAVORITES)

    def click_my_achivements(self):
        self.__click_button__(self.MY_ACHIVEMENTS)

    def click_my_comments(self):
        self.__click_button__(self.MY_COMMENTS)

    def click_my_review_awaits(self):
        self.__click_button__(self.MY_REVIEW_AWAITS)