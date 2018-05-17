from components.friends_list import FriendsList
from components.page import Page


class FriendsPage(Page):

	def __init__(self, driver, user_url):
		super(FriendsPage, self).__init__(driver)
		self.PAGE = user_url + '/friends'

	def open_message_dialog(self):
		friends_list = FriendsList(self.driver)
		friends_list.get_message_dialog_button().click()

	def friend_exists(self, url):
		friends_list = FriendsList(self.driver)
		friend = friends_list.find_friend_with_url(url)
		if friend is None:
			return False
		else:
			return True

