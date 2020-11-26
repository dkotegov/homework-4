import os
import time
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.feed import FeedPage
from pages.notification import Notification
from pages.profile import ProfilePage
from tests.login import LoginTest


class SubFeed(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        login_act = LoginTest()
        login_act.driver = self.driver
        login_act.loginBeforeAllTests()

        notif_page = Notification(self.driver)
        top_menu = notif_page.top_menu
        top_menu.go_to_my_profile()

        profile_page = ProfilePage(self.driver)
        profile_area = profile_page.profile_area
        sub_names = profile_area.get_my_subs_names()

        feed_page = FeedPage(self.driver)
        feed_area = feed_page.feed_area
        feed_area.show_sub()

        authors = feed_area.get_pins_authors()

        for check_author in authors:
            if check_author not in sub_names:
                self.assert_(False, check_author + " not your sub")
