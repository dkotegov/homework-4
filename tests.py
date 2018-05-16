import unittest

import os

import time
from selenium.webdriver import DesiredCapabilities, Remote

from constants import profiles
from pages.auth_page import AuthPage
# from pages.friends_page import FriendsPage
from pages.black_list_page import BlackList
from pages.friends_page import FriendsPage
from pages.main_page import MainPage
from time import sleep

from pages.message_page import MessagePage


class Tests(unittest.TestCase):

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
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        main_page = MainPage(self.driver)
        main_page.open_friends_list()

        friends_page = FriendsPage(self.driver)
        friends_page.open_message_dialog()

        message_page = MessagePage(self.driver)
        message_page.open_info_bar()
        message_page.add_to_black_list()
        message_page.accept_to_adding_to_black_list()

        auth_page.logout()
        auth_page.add_profile(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        main_page.open_friends_list()
        friends_page.open_message_dialog()
        message_page.send_message()

        # black_list = BlackList(self.driver)
        # black_list.open()
        sleep(3)
