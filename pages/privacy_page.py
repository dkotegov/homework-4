from components.page import Page
from components.privacy_component import PrivacyForm


class PrivacyPage(Page):

	def __init__(self, driver):
		super(PrivacyPage, self).__init__(driver)
		self.privacy_component = PrivacyForm(self.driver)
		self.PAGE = '/settings/privacy'

	def tag_my_in_photo_no_one(self):
		return self.privacy_component.get_radiobutton_by_name_and_value(self.privacy_component.TAG_ME_IN_PHOTO, self.privacy_component.NO_ONE)

	def tag_my_in_photo_only_friends(self):
		return self.privacy_component.get_radiobutton_by_name_and_value(self.privacy_component.TAG_ME_IN_PHOTO, self.privacy_component.ONLY_FRIENDS)

	def my_age_only_friends(self):
		return self.privacy_component.get_radiobutton_by_name_and_value(self.privacy_component.MY_AGE, self.privacy_component.ONLY_FRIENDS)	

	def my_age_all_users(self):
		return self.privacy_component.get_radiobutton_by_name_and_value(self.privacy_component.MY_AGE, self.privacy_component.ALL_USERS)

	def my_age_by_value(self, value):
		return self.privacy_component.get_radiobutton_by_name_and_value(self.privacy_component.MY_AGE, "@value = '"+ value + "'")				

	def save(self):
		return self.privacy_component.get_save_button()

	def is_cheked_element(self, radiobutton):
		return radiobutton.get_attribute("checked")

	def click(self, radiobutton):
		self.driver.execute_script("arguments[0].click();", radiobutton)
		
