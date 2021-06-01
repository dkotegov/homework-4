import unittest
from Pages.people_page import PeoplePage
from Pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from steps.auth import setup_auth

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
        self.profile_page.open_subscribers()
        self.profile_page.unsubscribe_from_profile()
        friend_list = self.profile_page.get_subscribe_list()
        self.assertNotIn(self.expected_friend, friend_list)

    def test_unsubscribe(self):
        self.people_page.open()
        self.people_page.unsubscribe()
        self.profile_page.open_subscribers()
        friend_list = self.profile_page.get_subscribe_list()
        self.assertNotIn(self.expected_friend, friend_list)


