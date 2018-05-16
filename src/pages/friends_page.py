from src.components.elements.friend_element import FriendsElement
from src.pages.base_page import BasePage


class FriendsPage(BasePage):

    def __init__(self, driver):
        super(FriendsPage, self).__init__(driver)
        self.element = FriendsElement(self.driver)

    def is_loaded(self):
        # TODO here you can add other logics
        is_marked = self.element.is_marked()
        return is_marked
