from components.main_vertical_list import MainVerticalList
from components.page import Page
from components.notification_component import NotificationComponent


class MainPage(Page):

	def __init__(self, driver):
		super(MainPage, self).__init__(driver)
		self.main_vertical_list = MainVerticalList(self.driver)

	def open_friends_list(self):
		self.main_vertical_list.get_friends().click()

	def accept_notification(self):
		notification = NotificationComponent(self.driver)
		notification.accept_reletionship().click()