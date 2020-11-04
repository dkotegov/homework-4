import unittest
from selenium import webdriver

from pages.leader_page import LeaderPage as page


class LeaderTests(unittest.TestCase):
    browser = webdriver.Chrome('./chromedriver')
    page = None

    @classmethod
    def setUpClass(cls):
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
