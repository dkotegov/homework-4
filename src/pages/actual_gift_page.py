from src.components.base_element import BaseElement
from src.components.elements.actual_gift_element import ActualGiftElement
from src.components.elements.gift_sent_element import GiftSentElement


class ActualGiftPage(BaseElement):

    def __init__(self, driver):
        super(ActualGiftPage, self).__init__(driver)
        self._url = 'https://ok.ru/gifts'
        self._element = ActualGiftElement(driver)
        self._gift_sent_element = GiftSentElement(driver)

    def is_loaded(self):
        return self._element.is_marked()

    def is_gift_sent(self):
        return self._gift_sent_element.is_gift_sent()
