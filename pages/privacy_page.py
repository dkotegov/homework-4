from components.page import Page
from components.privacy_component import PrivacyForm


class PrivacyPage(Page):

	def tag_my_in_photo_no_one(self):
		privacy_component = PrivacyForm(self.driver)
		radiobutton = privacy_component.get_radiobutton_by_name_and_value(PrivacyForm.TAG_MY_PHOTO, PrivacyForm.NO_ONE)
		self.driver.execute_script("arguments[0].click();", radiobutton)
	def tag_my_in_photo_only_friends(self):
		privacy_component = PrivacyForm(self.driver)
		radiobutton = privacy_component.get_radiobutton_by_name_and_value(PrivacyForm.TAG_MY_PHOTO, PrivacyForm.ONLY_FRIENDS)
		self.driver.execute_script("arguments[0].click();", radiobutton)
	def save(self):
		privacy_component = PrivacyForm(self.driver)
		save = privacy_component.get_save_button()
		save.click()	

		
