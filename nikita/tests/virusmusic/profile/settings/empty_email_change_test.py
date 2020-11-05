from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.settings import SettingsPage
from nikita.constants import PROFILE_DATA_EMAIL_ERROR, PROFILE_DATA_EMAIL_ERROR_EMPTY_MESSAGE
from nikita.utils import wait_for_element_attribute_change

class EmptyEmailChangeTest(Test):
    def test(self):
        page = SettingsPage(self.driver)
        page.change_email('')
        wait_for_element_attribute_change(
            self.driver,
            PROFILE_DATA_EMAIL_ERROR,
            'innerText',
            PROFILE_DATA_EMAIL_ERROR_EMPTY_MESSAGE
        )
