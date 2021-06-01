import unittest
from Pages.people_page import PeoplePage
from Pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from steps.auth import setup_auth



class SubscribeTests(unittest.TestCase):

    expected_friend = 'vileven'

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.people_page = PeoplePage(self.driver)
        self.profile_page = ProfilePage(self.driver)


    def tearDown(self):
        self.people_page.open()
        self.people_page.unsubscribe()
        self.driver.quit()

    def test_subscribe(self):
        self.people_page.open()
        self.people_page.subscribe()
        self.profile_page.open_subscribers()
        friend_list = self.profile_page.get_subscribe_list()
        self.assertIn(self.expected_friend, friend_list)
