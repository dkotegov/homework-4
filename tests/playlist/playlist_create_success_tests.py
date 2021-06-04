import unittest
from Pages.people_page import PeoplePage
from Pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from steps.auth import setup_auth



class PlaylistCreateSuccessTests(unittest.TestCase):
    playlist_name = "playlist"
    expected_notification_success = "Плэйлист успешно создан!"

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.open_playlist()


    def tearDown(self):
        self.profile_page.delete_last_playlist()
        self.driver.quit()

    def test_create_playlist_notification(self):
        self.profile_page.set_playlist(self.playlist_name)
        self.profile_page.submit_playlist()
        notification_text = self.profile_page.get_notification_text()
        self.assertEqual(notification_text, self.expected_notification_success)

    def test_create_playlist_name(self):
        self.profile_page.set_playlist(self.playlist_name)
        self.profile_page.submit_playlist()
        self.profile_page.get_notification_text()
        name = self.profile_page.get_last_playlist_name()
        self.assertEqual(name, self.playlist_name)

    def test_create_playlist_count(self):
        count_playlists_before_adding = self.profile_page.get_count_playlist()
        self.profile_page.set_playlist(self.playlist_name)
        self.profile_page.submit_playlist()
        self.profile_page.get_notification_text()
        count_playlists_after_adding = self.profile_page.get_count_playlist()
        self.assertLess(count_playlists_before_adding, count_playlists_after_adding)
