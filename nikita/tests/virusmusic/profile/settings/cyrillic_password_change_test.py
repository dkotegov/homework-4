import os

from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.settings import SettingsPage
from nikita.constants import NEW_PASSWORD_ERROR, NEW_PASSWORD_ERROR_LENGTH_MESSAGE
from nikita.utils import wait_for_element_attribute_change

class CyrillicPasswordChangeTest(Test):
    NEW_PASSWORD = 'лол'
    NEW_PASSWORD_CONFIRM = 'лол'
    PASSWORD = os.environ['PASSWORD']

    def test(self):
        page = SettingsPage(self.driver)
        page.change_password(
            self.NEW_PASSWORD,
            self.NEW_PASSWORD_CONFIRM,
            self.PASSWORD
        )
        wait_for_element_attribute_change(
            self.driver,
            NEW_PASSWORD_ERROR,
            'innerText',
            NEW_PASSWORD_ERROR_LENGTH_MESSAGE
        )
