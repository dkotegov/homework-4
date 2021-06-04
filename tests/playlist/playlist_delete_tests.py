import unittest
from Pages.people_page import PeoplePage
from Pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from steps.auth import setup_auth



class PlaylistDeleteTests(unittest.TestCase):
    playlist_name = "playlist"
    expected_notification_delete_playlist = "Плейлист удалён"

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.create_playlist(self.playlist_name)


    def tearDown(self):
        self.driver.quit()

    def test_delete_playlist_notification(self):
        self.profile_page.delete_last_playlist()
        notification_text = self.profile_page.get_notification_text()
        self.assertEqual(notification_text, self.expected_notification_delete_playlist)

    def test_delete_playlist_count(self):
        count_playlists_before_delete = self.profile_page.get_count_playlist()
        self.profile_page.delete_last_playlist()
        self.profile_page.get_notification_text()
        count_playlists_after_delete = self.profile_page.get_count_playlist()
        self.assertGreater(count_playlists_before_delete, count_playlists_after_delete)
