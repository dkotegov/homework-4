from src.components.elements.feed_element import FeedElement
from src.pages.base_page import BasePage


class FeedPage(BasePage):

    def __init__(self, driver):
        super(FeedPage, self).__init__(driver)
        self.element = FeedElement(self.driver)
        self._url = 'ok.ru/feed'

    def is_loaded(self):
        # TODO here you can add a search for other items
        is_exists_nav_side = self.element.is_exist_nav_side()
        return is_exists_nav_side
