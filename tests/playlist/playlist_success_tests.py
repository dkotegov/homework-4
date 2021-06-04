import unittest
from Pages.people_page import PeoplePage
from Pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from steps.auth import setup_auth



class SubscribeTests(unittest.TestCase):
    playlist_name = "playlist"
    empty_playlist_name = ""
    success_notification = "Плэйлист успешно создан!"
    empty_name_notification = "Пустое название!"

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.open_playlist()


    def tearDown(self):
        self.driver.quit()

    def test_create_playlist_notification(self):
        self.profile_page.set_playlist(self.playlist_name)
        self.profile_page.submit_playlist()
        friend_list = self.get
        self.assertIn(self.expected_friend, friend_list)
