import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from src.pages.main_page import MainPage


class MainPageTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.main_page = MainPage(self.driver)
        self.main_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_open_gifts(self):
        gifts_page = self.main_page.open_gifts()
        ok = gifts_page.is_loaded()
        self.assertTrue(ok)

    def test_open_friend_and_make_gift(self):
        friends_page = self.main_page.open_friends()
        friend_profile = friends_page.open_friend_profile()
        gift_page = friend_profile.make_gift()
        ok = gift_page.is_loaded()
        self.assertTrue(ok)

        gift_page = gift_page.send_gift_with_selected_profile()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)
