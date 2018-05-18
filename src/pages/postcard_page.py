from src.components.base_element import BaseElement
from src.components.elements.postcard_element import PostCardElement


class PostCardPage(BaseElement):

    def __init__(self, driver):
        super(PostCardPage, self).__init__(driver)
        self._url = 'https://ok.ru/gifts/liveGifts'
        self._element = PostCardElement(driver)

    def is_loaded(self):
        return self._element.is_exists_gird()
