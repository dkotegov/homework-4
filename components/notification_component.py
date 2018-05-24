# -*- coding: utf-8 -*-
from components.base_component import BaseComponent


class NotificationComponent(BaseComponent):
	ACCEPT = "//span[@class = 'al growl_open' and @data-l = 't,growl_link']"


	def accept_reletionship(self):
		return self.get_clickable_element(self.ACCEPT)