import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from src.pages.gift_page import GiftPage


class GiftsPageTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.gift_page = GiftPage(self.driver)
        self.gift_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_open_feed_page_by_logo(self):
        feed_page = self.gift_page.open_feed_page_by_logo()
        ok = feed_page.is_loaded()
        self.assertTrue(ok)

    def test_open_feed_page_by_nav_menu(self):
        feed_page = self.gift_page.open_feed_page_by_nav_menu()
        ok = feed_page.is_loaded()
        self.assertTrue(ok)

    def test_open_friends_page_by_nav_menu(self):
        friends_page = self.gift_page.open_friends_page_by_nav_menu()
        ok = friends_page.is_loaded()
        self.assertTrue(ok)

    def test_open_photo_page_by_nav_menu(self):
        photo_page = self.gift_page.open_photo_page_by_nav_menu()
        ok = photo_page.is_loaded()
        self.assertTrue(ok)

    def test_open_groups_page_by_nav_menu(self):
        groups_page = self.gift_page.open_groups_page_by_nav_menu()
        ok = groups_page.is_loaded()
        self.assertTrue(ok)

    def test_open_games_page_by_nav_menu(self):
        games_page = self.gift_page.open_games_page_by_nav_menu()
        ok = games_page.is_loaded()
        self.assertTrue(ok)

    def test_open_notes_page_by_nav_menu(self):
        notes_page = self.gift_page.open_notes_page_by_nav_menu()
        ok = notes_page.is_loaded()
        self.assertTrue(ok)

    def test_open_inventories_page_by_nav_menu(self):
        inventories_page = self.gift_page.open_inventories_page_by_nav_menu()
        ok = inventories_page.is_loaded()
        self.assertTrue(ok)

    def test_open_own_gifts_page_by_nav_menu(self):
        own_gifts_page = self.gift_page.open_own_gifts()
        ok = own_gifts_page.is_loaded()
        self.assertTrue(ok)

        ok = own_gifts_page.is_loaded_own_gifts()
        self.assertTrue(ok)
