import time
import unittest

from selenium import webdriver
from Pages.auth_page import AuthPage
from Pages.profile_page import ProfilePage


class PlaylistTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_create_playlist(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        profile_page = ProfilePage(self.driver)
        profile_page.open_playlist()
        playlist_name = "123"
        profile_page.set_playlist(playlist_name)
        profile_page.submit_playlist()
        check = profile_page.check_playlist(playlist_name)
        profile_page.delete_playlist()
        self.assertEqual(check, True)

    def test_create_playlist_empty_name(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        profile_page = ProfilePage(self.driver)
        profile_page.open_playlist()
        before = profile_page.get_count_playlist()
        profile_page.set_playlist("")
        profile_page.submit_playlist()
        after = profile_page.get_count_playlist()
        self.assertEqual(before == after, True)


