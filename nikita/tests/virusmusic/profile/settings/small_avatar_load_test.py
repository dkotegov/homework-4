import os

from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.settings import SettingsPage
from nikita.utils import wait_for_pop_up

class SmallAvatarLoadTest(Test):
    SMALL_AVATAR_PATH = os.getcwd() + '/nikita/resources/small_avatar.png'

    def test(self):
        page = SettingsPage(self.driver)
        page.load_avatar(self.SMALL_AVATAR_PATH)
        wait_for_pop_up(self.driver)
