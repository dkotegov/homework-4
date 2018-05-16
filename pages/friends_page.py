from components.friends_list import FriendsList
from components.page import Page


class FriendsPage(Page):

    def open_message_dialog(self):
        friends_list = FriendsList(self.driver)
        friends_list.get_message_dialog_button().click()
