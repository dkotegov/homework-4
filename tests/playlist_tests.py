import time
import unittest
import os

from selenium.webdriver import DesiredCapabilities, Remote
from selenium import webdriver
from Pages.auth_page import AuthPage
from Pages.profile_page import ProfilePage
from Pages.film_page import FilmPage


class PlaylistTests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_create_playlist(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        profile_page = ProfilePage(self.driver)
        playlist_name = "123"
        profile_page.create_playlist(playlist_name)
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

    def test_add_film_in_playlist(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        profile_page = ProfilePage(self.driver)
        playlist_name = "123"
        profile_page.create_playlist(playlist_name)
        profile_page.wait_playlist_create()
        film_page = FilmPage(self.driver)
        film_page.open()
        film_page.add_film_in_playlist()
        check = film_page.check_adding_in_playlist_succes()
        profile_page.open_playlist()
        profile_page.check_film_in_playlist()
        profile_page.delete_playlist()
        self.assertEqual(check, True)

    def test_add_film_in_playlist_exist(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        profile_page = ProfilePage(self.driver)
        playlist_name = "123"
        profile_page.create_playlist(playlist_name)
        profile_page.wait_playlist_create()
        film_page = FilmPage(self.driver)
        film_page.open()
        film_page.add_film_in_playlist()
        film_page.add_film_in_playlist()
        check = film_page.check_adding_in_playlist_exist()
        profile_page.open_playlist()
        profile_page.delete_playlist()
        self.assertEqual(check, True)

    def test_delete_film(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        profile_page = ProfilePage(self.driver)
        playlist_name = "123"
        profile_page.create_playlist(playlist_name)
        profile_page.wait_playlist_create()
        film_page = FilmPage(self.driver)
        film_page.open()
        film_page.add_film_in_playlist()
        film_page.check_adding_in_playlist_succes()
        profile_page.open_playlist()
        before = profile_page.get_count_film_in_playlist()
        profile_page.delete_film_from_playlist()
        profile_page.wait_film_delete()
        after = profile_page.get_count_film_in_playlist()
        profile_page.delete_playlist()
        self.assertEqual(before - after, 1)

    def test_delete_playlist(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        profile_page = ProfilePage(self.driver)
        playlist_name = "123"
        profile_page.create_playlist(playlist_name)
        profile_page.wait_playlist_create()
        before = profile_page.get_count_playlist()
        profile_page.delete_playlist()
        profile_page.wait_playlist_delete()
        after = profile_page.get_count_playlist()
        self.assertEqual(before - after, 1)
