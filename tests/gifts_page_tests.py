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
    #
    # def test_open_feed_page_by_logo(self):
    #     feed_page = self.gift_page.open_feed_page_by_logo()
    #     ok = feed_page.is_loaded()
    #     self.assertTrue(ok)

    # def test_open_feed_page_by_nav_menu(self):
    #     feed_page = self.gift_page.open_feed_page_by_nav_menu()
    #     ok = feed_page.is_loaded()
    #     self.assertTrue(ok)

    def test_open_friends_page_by_nav_menu(self):
        friends_page = self.gift_page.open_friends_page_by_nav_menu()
        ok = friends_page.is_loaded()
        self.assertTrue(ok)
