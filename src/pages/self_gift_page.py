from src.components.base_element import BaseElement
from src.components.elements.self_gift_element import SelfGiftElement
from src.pages.auth_page import AuthPage


class SelfGiftPage(BaseElement):

    def __init__(self, driver):
        super(SelfGiftPage, self).__init__(driver)
        self._url = 'http://ok.ru/gifts/my'
        self._self_gift_element = SelfGiftElement(driver)
        self._auth_page = AuthPage(driver)

    def is_loaded(self):
        return self._self_gift_element.is_marked()

    def like_gift(self):
        self._self_gift_element.get_like_button().click()
        return

    def open_gift_dialog(self):
        self._self_gift_element.get_dialog_button().click()
        return

    def open(self):
        self._auth_page.open_and_sign_in()
        self.driver.get(self._url)
