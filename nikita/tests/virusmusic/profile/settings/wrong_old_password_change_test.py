from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.settings import SettingsPage
from nikita.constants import PASSWORD_ERROR, PASSWORD_ERROR_WRONG_OLD_MESSAGE
from nikita.utils import wait_for_element_attribute_change

class WrongOldPasswordChangeTest(Test):
    NEW_PASSWORD = 'lol'
    NEW_PASSWORD_CONFIRM = 'lol'
    PASSWORD = 'kek'

    def test(self):
        page = SettingsPage(self.driver)
        page.change_password(
            self.NEW_PASSWORD,
            self.NEW_PASSWORD_CONFIRM,
            self.PASSWORD
        )
        wait_for_element_attribute_change(
            self.driver,
            PASSWORD_ERROR,
            'innerText',
            PASSWORD_ERROR_WRONG_OLD_MESSAGE
        )
