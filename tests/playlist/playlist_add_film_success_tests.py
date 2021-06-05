import unittest
from Pages.film_page import FilmPage
from Pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from steps.auth import setup_auth


class AddFilmInPlaylistSuccessTests(unittest.TestCase):
    playlist_name = "playlist"
    expected_notification_success = "Вы успешно добавили фильм в плэйлист"

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.create_playlist(self.playlist_name)
        self.film_page = FilmPage(self.driver)
        self.film_page.open()

    def tearDown(self):
        self.profile_page.open_playlist()
        self.profile_page.delete_last_playlist()
        self.driver.quit()

    def test_add_film_in_playlist_notification(self):
        self.film_page.select_playlist(self.playlist_name)
        self.film_page.submit_to_add_in_playlist()
        notification = self.film_page.get_notification_text()
        self.assertEqual(notification, self.expected_notification_success)

    def test_add_film_in_playlist_id(self):
        self.film_page.select_playlist(self.playlist_name)
        self.film_page.submit_to_add_in_playlist()
        self.film_page.get_notification_text()
        self.profile_page.open()
        self.assertTrue(self.profile_page.check_film_in_playlist())

    def test_add_film_in_playlist_count(self):
        self.profile_page.open()
        count_film_before = self.profile_page.get_count_film_in_playlist()
        self.film_page.open()
        self.film_page.select_playlist(self.playlist_name)
        self.film_page.submit_to_add_in_playlist()
        self.film_page.get_notification_text()
        self.profile_page.open()
        count_film_after = self.profile_page.get_count_film_in_playlist()
        self.assertLess(count_film_before, count_film_after)
