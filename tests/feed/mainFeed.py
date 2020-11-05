import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.feed import FeedPage
from tests.login import LoginTest


class MainFeed(unittest.TestCase):

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

        feed_page = FeedPage(self.driver)
        feed_page.open()

        self.driver.refresh()

        feed_area = feed_page.feed_area

        have_before_scroll = feed_area.get_pins_count()

        feed_area.scroll()

        have_after_scroll = feed_area.get_pins_count()

        self.assert_(have_before_scroll*2 == have_after_scroll)


