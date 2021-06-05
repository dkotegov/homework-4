import unittest
from Pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from steps.auth import setup_auth


class PlaylistCreateWrongTests(unittest.TestCase):
    empty_playlist_name = ""
    expected_notification_empty_name = "Пустое название!"

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.open_playlist()

    def tearDown(self):
        self.driver.quit()

    def test_create_playlist_notification(self):
        self.profile_page.set_playlist(self.empty_playlist_name)
        self.profile_page.submit_playlist()
        notification_text = self.profile_page.get_notification_text()
        self.assertEqual(notification_text, self.expected_notification_empty_name)

    def test_create_playlist_count(self):
        count_playlists_before_adding = self.profile_page.get_count_playlist()
        self.profile_page.set_playlist(self.empty_playlist_name)
        self.profile_page.submit_playlist()
        self.profile_page.get_notification_text()
        count_playlists_after_adding = self.profile_page.get_count_playlist()
        self.assertEqual(count_playlists_before_adding, count_playlists_after_adding)
