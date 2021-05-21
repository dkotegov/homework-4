import unittest
from Pages.people_page import PeoplePage
from Pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from steps.auth import setup_auth
from utils.not_in import not_in

class UnsubscribeTests(unittest.TestCase):

    expected_friend = 'vileven'

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.people_page = PeoplePage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.people_page.open()
        self.people_page.subscribe()


    def tearDown(self):
        self.driver.quit()

    def test_unsubscribe_from_profile(self):
        self.profile_page.unsubscribe_from_profile()
        friend_list = self.profile_page.get_subscribe_list()
        is_unsub = not_in(self.expected_friend, friend_list)
        self.assertTrue(is_unsub)

    def test_unsubscribe(self):
        self.people_page.open()
        self.people_page.unsubscribe()
        friend_list = self.profile_page.get_subscribe_list()
        is_unsub = not_in(self.expected_friend, friend_list)
        self.assertTrue(is_unsub)


