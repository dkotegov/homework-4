from src.components.elements.main_element import MainElement
from src.pages.auth_page import AuthPage
from src.pages.base_page import BasePage
from src.pages.gift_page import GiftPage


class MainPage(BasePage):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self._url = 'https://ok.ru/'
        self.main_element = MainElement(self.driver)
        self._auth_page = AuthPage(driver)

    def open_gifts(self):
        self.main_element.get_gifts_button().click()
        return GiftPage(self.driver)

    def open_friends(self):
        self.main_element.get_friends_button().click()
        return FriendsPage(self.driver)

    def open(self):
        self._auth_page.open_and_sign_in()
        self.driver.get(self._url)

from src.pages.friends_page import FriendsPage
