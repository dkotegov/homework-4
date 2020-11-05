import os
import time
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.feed import FeedPage
from pages.notification import Notification
from pages.profile import ProfilePage


class GetUserPinsNoLogin(unittest.TestCase):

    LOAD_MSG = 'Что-то пошло не так с пинами пользователя'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):

        notif_page = Notification(self.driver)
        top_menu = notif_page.top_menu
        top_menu.go_to_sup_profile()

        profile_page = ProfilePage(self.driver)
        profile_area = profile_page.profile_area
        profile_area.click_my_pins()

        feed_page = FeedPage(self.driver)

        feed_area = feed_page.feed_area
        load_msg = feed_area.get_load_msg()

        self.assertEqual(load_msg, self.LOAD_MSG)
