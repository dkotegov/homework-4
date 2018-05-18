from src.components.base_element import BaseElement
from src.components.elements.actual_gift_element import ActualGiftElement


class ActualGiftPage(BaseElement):

    def __init__(self, driver):
        super(ActualGiftPage, self).__init__(driver)
        self._url = 'https://ok.ru/gifts'
        self._element = ActualGiftElement(driver)

    def is_loaded(self):
        return self._element.is_marked()
