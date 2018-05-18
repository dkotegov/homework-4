from components.base_component import BaseComponent


class NotificationComponent(BaseComponent):
	NOTIFICATION = "//div[@class='toolbar_nav_i_tx-w usel-off']"
	ACCEPT = "//button[@data-l = 't,btn_accept']"

	def notification(self):
		return self.get_clickable_element(self.NOTIFICATION)

	def accept_reletionship(self):
		return self.get_clickable_element(self.ACCEPT)