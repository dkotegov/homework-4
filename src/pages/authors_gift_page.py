from src.components.base_element import BaseElement
from src.components.elements.authors_gift_element import AuthorsGiftElement


class AuthorsGiftPage(BaseElement):

    def __init__(self, driver):
        super(AuthorsGiftPage, self).__init__(driver)
        self._url = 'https://ok.ru/gifts/authorGifts'
        self._element = AuthorsGiftElement(driver)

    def is_loaded(self):
        return self._element.is_exists_gird()
