import os

import unittest
from selenium import webdriver
import urllib.parse as urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from Pages.auth_page import AuthPage
from Pages.people_page import PeoplePage
from Pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from steps.auth import setup_auth
from steps.logout import logout
from Pages.settings_page import SettingPage


class SubscribeTests(unittest.TestCase):

    expected_friend = 'vileven'

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.people_page = PeoplePage(self.driver)
        self.profile_page = ProfilePage(self.driver)


    def tearDown(self):
        self.people_page.unsubscribe()
        self.driver.quit()

    def test_subscribe(self):
        self.people_page.subscribe()
        self.driver.refresh()
        friend_login = self.profile_page.get_friend_login()
        self.assertEqual(friend_login, self.expected_friend)

    # def test_unsubscribe(self):
    #     path = 'people/17'
    #     auth_page = AuthPage(self.driver)
    #     auth_page.auth()
    #     people_page = PeoplePage(self.driver)
    #     people_page.PATH = '/' + path
    #     people_page.sub_and_unsub()
    #     auth_page.logout()
    #     auth_page.auth()
    #     profile_page = ProfilePage(self.driver)
    #     profile_page.check_unsub(path)
    #
    # def test_unsubscribe_from_profile(self):
    #     path = 'people/17'
    #     id = 'profile/17'
    #     auth_page = AuthPage(self.driver)
    #     auth_page.auth()
    #     people_page = PeoplePage(self.driver)
    #     people_page.PATH = '/' + path
    #     people_page.subscribe()
    #     auth_page.logout()
    #     auth_page.auth()
    #     profile_page = ProfilePage(self.driver)
    #     profile_page.unsub(id)

