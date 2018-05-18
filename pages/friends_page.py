from components.friends_list import FriendsList
from components.page import Page
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class FriendsPage(Page):

	def __init__(self, driver, user_url):
		super(FriendsPage, self).__init__(driver)
		self.user_url = user_url
		self.PAGE = user_url + '/friends'

	def open_message_dialog(self):
		friends_list = FriendsList(self.driver)
		friends_list.get_message_dialog_button().click()

	def subscribers_visibility(self):
		try:
			friends_list = FriendsList(self.driver)
			friends_list.subscribers_list(self.user_url)
			return True
		except TimeoutException:
			return False    

	def subscriptions_visibility(self):
		try:
			friends_list = FriendsList(self.driver)
			friends_list.subscriptions_list(self.user_url)
			return True
		except TimeoutException:
			return False  
