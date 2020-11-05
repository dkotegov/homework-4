import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.feed import FeedPage
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

        feed_page = FeedPage(self.driver)
        feed_area = feed_page.feed_area
        feed_area.show_sub()

        feed_area.get_pins_count()  # don't check return value, err if not found columns div

        self.driver.refresh()

        feed_area.get_pins_count()




