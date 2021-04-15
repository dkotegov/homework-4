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
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_subscribe(self):
        path = 'people/17'
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        people_page = PeoplePage(self.driver)
        people_page.PATH = '/' + path
        people_page.subscribe()
        auth_page.logout()
        auth_page.auth()
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
        auth_page.logout()
        auth_page.auth()
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
        auth_page.logout()
        auth_page.auth()
        profile_page = ProfilePage(self.driver)
        profile_page.unsub(id)

