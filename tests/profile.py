from utils.helpers import if_element_exists, wait_for_visible
from pages.login import LoginPage
from pages.profile import ProfilePage
from tests.base import BaseTest


class ProfileTestSuite(BaseTest):
    # def test_create_playlist(self):
    #     login = LoginPage(self.driver)
    #     profile = ProfilePage(self.driver)
    #
    #     login.open()
    #     login.sign_in()
    #     wait_for_visible(self.driver, login.USER_NAME_HEADER)
    #
    #     profile.open()
    #     playlist_name = 'New Playlist'
    #     old_playlists = profile.playlists
    #     profile.create_playlist(playlist_name)
    #     new_playlists = profile.playlists
    #
    #     self.assertEqual(len(new_playlists) - len(old_playlists), 1)
    #     self.assertEqual(new_playlists[-1], playlist_name.upper())

    def test_cancel_create_playlist(self):
        login = LoginPage(self.driver)
        profile = ProfilePage(self.driver)

        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        profile.open()
        playlist_name = 'New Playlist'
        old_len = len(profile.playlists)
        profile.cancel_create_playlist(playlist_name)

        self.assertEqual(len(profile.playlists), old_len)
        self.assertFalse(if_element_exists(self.driver, profile.create_playlist_form))

    def test_no_follow_for_unauthorized(self):
        profile = ProfilePage(self.driver, 'IlyaAfimin')

        profile.open()

        self.assertFalse(if_element_exists(self.driver, profile.FOLLOW_BUTTON))

    def test_follow_user(self):
        login = LoginPage(self.driver)
        profile = ProfilePage(self.driver, 'IlyaAfimin')

        login.open()
        login.sign_in()

        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        profile.open()
        self.assertEqual(profile.follow_button.text.lower(), 'подписаться')

        old_followers = profile.followers
        profile.toggle_follow()
        new_followers = profile.followers
        try:
            self.assertEqual(profile.follow_button.text.lower(), 'отписаться')
            self.assertEqual(new_followers - old_followers, 1)
        finally:
            profile.toggle_follow()

    def test_unfollow_user(self):
        login = LoginPage(self.driver)
        profile = ProfilePage(self.driver, 'IlyaAfimin')

        login.open()
        login.sign_in()

        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        profile.open()
        old_followers = profile.followers
        profile.toggle_follow()
        try:
            self.assertEqual(profile.follow_button.text.lower(), 'отписаться')
        except:
            profile.toggle_follow()
            return

        new_followers = profile.followers
        profile.toggle_follow()

        self.assertEqual(profile.follow_button.text.lower(), 'подписаться')
        self.assertEqual(new_followers - old_followers, 1)
