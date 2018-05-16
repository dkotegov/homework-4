from src.components.base_element import BaseElement
from src.components.elements.gift_element import GiftElement


class GiftPage(BaseElement):

    def __init__(self, driver):
        super(GiftPage, self).__init__(driver)
        self._url = 'http://ok.ru/gifts'
        self._gift_element = GiftElement(driver)

    def is_loaded(self):
        return self._gift_element.is_marked()
