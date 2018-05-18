from src.pages.base_page import BasePage
from src.components.elements.friend_element import FriendsElement



class FriendsPage(BasePage):

    def __init__(self, driver):
        super(FriendsPage, self).__init__(driver)
        self.element = FriendsElement(self.driver)


    def is_loaded(self):
        # TODO here you can add other logic
        is_marked = self.element.is_marked()
        return is_marked

    def open_friend_profile(self):
        btn = self.element.get_friend_ico()
        btn.click()
        return FriendProfilePage(self.driver)

from src.pages.friend_profile_page import FriendProfilePage
