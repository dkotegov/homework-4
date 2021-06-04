import unittest
from Pages.film_page import FilmPage
from Pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from steps.auth import setup_auth



class DeleteFilmFromPlaylistTests(unittest.TestCase):
    playlist_name = "playlist"
    expected_notification_delete_playlist = "Фильм удален"

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.create_playlist(self.playlist_name)
        self.film_page = FilmPage(self.driver)
        self.film_page.add_film_in_playlist(self.playlist_name)
        self.profile_page.open()


    def tearDown(self):
        self.profile_page.delete_last_playlist()
        self.driver.quit()

    def test_delete_playlist_notification(self):
        self.profile_page.delete_film_from_playlist()
        notification_text = self.profile_page.get_notification_text()
        self.assertEqual(notification_text, self.expected_notification_delete_playlist)

