from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.settings import SettingsPage
from nikita.constants import PROFILE_DATA_NAME_ERROR, PROFILE_DATA_NAME_ERROR_MESSAGE
from nikita.utils import wait_for_element_attribute_change

class EmptyNameChangeTest(Test):
    def test(self):
        page = SettingsPage(self.driver)
        page.change_name('')
        wait_for_element_attribute_change(
            self.driver,
            PROFILE_DATA_NAME_ERROR,
            'innerText',
            PROFILE_DATA_NAME_ERROR_MESSAGE
        )
