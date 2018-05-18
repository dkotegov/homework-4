from src.components.elements.main_element import MainElement
from src.pages.auth_page import AuthPage
from src.pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.element = MainElement(self.driver)
        self.auth_page = AuthPage(driver)

    def open(self):
        self.auth_page.open_and_sign_in()

    def open_gifts(self):
        self.element.get_gifts_button().click()
        return GiftPage(self.driver)

    def is_loaded(self):
        is_exists_nav_side = self.element.is_exist_nav_side()
        return is_exists_nav_side

from src.pages.gift_page import GiftPage