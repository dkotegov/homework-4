from components.friends_list import FriendsList
from pages.page import Page


class FriendsPage(Page):

    def open_message_dialog_with_55(self):
        friends_list = FriendsList(self.driver)
        friends_list.get_message_with_55_dialog_button().click()

    def open_message_dialog_with_46(self):
        friends_list = FriendsList(self.driver)
        friends_list.get_message_with_46_dialog_button().click()
