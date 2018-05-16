from components.page import Page
from components.privacy_component import PrivacyForm


class PrivacyPage(Page):

	def test(self):
		privacy_component = PrivacyForm(self.driver)
		radiobutton = PrivacyForm.get_radiobutton_by_name_and_value(privacy_component, PrivacyForm.TAG_MY_PHOTO, PrivacyForm.NO_ONE)
		#radiobutton.location_once_scrolled_into_view
		#radiobutton.click()
