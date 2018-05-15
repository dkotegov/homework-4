import unittest

import os

import time
from selenium.webdriver import DesiredCapabilities, Remote

from pages.auth_page import AuthPage
# from pages.friends_page import FriendsPage
from pages.main_page import MainPage


class Tests(unittest.TestCase):
    PROFILE_ONE_LOGIN = 'technopark43'
    PROFILE_PASSWORD = os.environ['PROFILE_PASSWORD']
    PROFILE_SECOND_LOGIN = 'technopark46'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_add_profile_to_black_list(self):
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(self.PROFILE_ONE_LOGIN, self.PROFILE_PASSWORD)

        main_page = MainPage(self.driver)
        main_page.open_friends_list()

        #friends_page = FriendsPage(self.driver)
        # friends_page = FriendsPage(self.driver)
        # friends = friends_page.friends_list
        # friends.open_friends_list()
