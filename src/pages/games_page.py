from src.pages.base_page import BasePage
from src.components.elements.games_element import GamesElement


class GamesPage(BasePage):

    def __init__(self, driver):
        super(GamesPage, self).__init__(driver)
        self.element = GamesElement(self.driver)

    def is_loaded(self):
        # TODO here you can add other logic
        is_marked = self.element.is_marked()
        return is_marked
