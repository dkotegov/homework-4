import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote

from selenium import webdriver

from pages.leader_page import LeaderPage as page


class LeaderTests(unittest.TestCase):
    browser = None
    page = None

    @classmethod
    def setUpClass(cls):
        browser_name = os.environ.get('BROWSER', 'CHROME')
        LeaderTests.browser = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser_name).copy()
        )
        LeaderTests.page = page(LeaderTests.browser)
        LeaderTests.page.login()

    def test_user_data(self):
        self.page.open_leader_page()
        self.page.select_all_time_range_filter()
        user_score = self.page.get_user_score()
        user_profile_score = self.page.focus_on_user()
        self.assertGreaterEqual(user_profile_score, user_score)

    @classmethod
    def tearDownClass(cls):
        LeaderTests.browser.quit()
