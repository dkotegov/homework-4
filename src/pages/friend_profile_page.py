from src.components.elements.friend_profile_element import FriendProfileElement
from src.pages.base_page import BasePage
from src.pages.gift_page import GiftPage


class FriendProfilePage(BasePage):

    def __init__(self, driver):
        super(FriendProfilePage, self).__init__(driver)
        self.element = FriendProfileElement(self.driver)


    def make_gift(self):
        btn = self.element.get_make_gift_ico()
        btn.click()
        return GiftPage(self.driver)

