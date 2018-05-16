from src.components.base_element import BaseElement
from src.components.elements.gift_element import GiftElement
from src.pages.auth_page import AuthPage


class GiftPage(BaseElement):

    def __init__(self, driver):
        super(GiftPage, self).__init__(driver)
        self._url = 'http://ok.ru/gifts'
        self._element = GiftElement(driver)
        self._auth_page = AuthPage(driver)

    def is_loaded(self):
        return self._element.is_marked()

    def open(self):
        self._auth_page.open_and_sign_in()
        self.driver.get(self._url)

    def open_main_page(self):
        self._element.get_logo().click()
        return MainPage(self.driver)

from .main_page import MainPage