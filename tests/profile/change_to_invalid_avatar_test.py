import os

from pages.profile import ProfilePage
from tests.default_authorized import TestAuthorized


class ChangeToInvalidAvatarTest(TestAuthorized):
    PATH_OF_INVALID_AVATAR = os.getcwd() + '/resources/invalid_avatar.pdf'
    PATH_OF_DEFAULT_AVATAR = 'https://redioteka.com/assets/profile.webp'

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_page.upload_new_avatar(self.PATH_OF_INVALID_AVATAR)
        profile_page.save_avatar()

        self.assertEqual(
            self.PATH_OF_DEFAULT_AVATAR,
            profile_page.get_current_avatar()
        )
