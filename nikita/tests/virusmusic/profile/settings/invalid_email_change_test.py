from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.settings import SettingsPage
from nikita.constants import PROFILE_DATA_EMAIL_ERROR, PROFILE_DATA_EMAIL_ERROR_INVALID_MESSAGE
from nikita.utils import wait_for_element_attribute_change

class InvalidEmailChangeTest(Test):
    INVALID_EMAIL = 'lolkek.ru'

    def test(self):
        page = SettingsPage(self.driver)
        page.change_email(self.INVALID_EMAIL)
        wait_for_element_attribute_change(
            self.driver,
            PROFILE_DATA_EMAIL_ERROR,
            'innerText',
            PROFILE_DATA_EMAIL_ERROR_INVALID_MESSAGE
        )
