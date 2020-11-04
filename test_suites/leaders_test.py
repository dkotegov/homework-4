import unittest

from pages.leader_page import LeaderPage as page


class LeaderTests(unittest.TestCase):

    def test_a_setup(self):
        self.page = page()
        self.page.login()

    def test_user_data(self):
        self.page = page()
        self.page.open_leader_page()
        self.page.select_all_time_range_filter()
        self.page.compare_scores()
