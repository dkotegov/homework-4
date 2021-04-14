import os

import unittest
from selenium import webdriver
import urllib.parse as urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from Pages.auth_page import AuthPage
from Pages.people_page import PeoplePage
from Pages.profile_page import ProfilePage
from Pages.settings_page import SettingPage


class SubscribeTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_subscribe(self):
        path = 'people/17'
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        people_page = PeoplePage(self.driver)
        people_page.PATH = '/' + path
        people_page.subscribe()
        profile_page = ProfilePage(self.driver)
        profile_page.check_sub(path)
        people_page.unsubscribe()

    def test_unsubscribe(self):
        path = 'people/17'
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        people_page = PeoplePage(self.driver)
        people_page.PATH = '/' + path
        people_page.sub_and_unsub()
        profile_page = ProfilePage(self.driver)
        profile_page.check_unsub(path)

    def test_unsubscribe_from_profile(self):
        path = 'people/17'
        id = 'profile/17'
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        people_page = PeoplePage(self.driver)
        people_page.PATH = '/' + path
        people_page.subscribe()
        profile_page = ProfilePage(self.driver)
        profile_page.unsub(id)

    def test_avatar(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth_custom(auth_page.SIGNUP_LOGIN, "12345678")
        settings_page = SettingPage(self.driver)
        settings_page.open()
        avatar = settings_page.setup_avatar()
        settings_page.submit()
        self.assertEqual(avatar, "C:\\fakepath\\vorobey.jpg")
