from src.components.base_element import BaseElement
from src.components.elements.create_gift_element import CreateGiftElement


class CreateGiftPage(BaseElement):

    def __init__(self, driver):
        super(CreateGiftPage, self).__init__(driver)
        self._url = 'https://ok.ru/app/constructor'
        self._element = CreateGiftElement(driver)

    def is_loaded(self):
        return self._element.is_exists_grid()
