import unittest

import os

import time
from selenium.webdriver import DesiredCapabilities, Remote

from constants import profiles, dialog
from pages.auth_page import AuthPage
# from pages.friends_page import FriendsPage
from pages.black_list_page import BlackList, BlackListPage
from pages.friends_page import FriendsPage
from pages.game_page import GamePage
from pages.games_vitrine import GamesVitrine
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

    # def test_add_profile_to_and_delete_from_black_list(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)
    #
    #     main_page = MainPage(self.driver)
    #     main_page.open_friends_list()
    #
    #     friends_page = FriendsPage(self.driver)
    #     friends_page.open_message_dialog()
    #
    #     message_page = MessagePage(self.driver)
    #     message_page.open_info_bar()
    #     message_page.add_to_black_list()
    #     message_page.accept_to_adding_to_black_list()
    #
    #     auth_page.logout()
    #
    #     auth_page.add_profile()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)
    #
    #     main_page.open_friends_list()
    #     friends_page.open_message_dialog()
    #     message_page.send_message()
    #
    #     auth_page.logout()
    #
    #     auth_page.add_profile()
    #     auth_page.clear_inputs()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)
    #
    #     main_page.open_friends_list()
    #     friends_page.open_message_dialog()
    #
    #     self.assertFalse(message_page.check_message(), False)
    #
    #     # delete
    #     black_list = BlackListPage(self.driver)
    #     black_list.open()
    #     black_list.delete_from()
    #
    #     auth_page.logout()
    #
    #     auth_page.add_profile()
    #     auth_page.clear_inputs()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)
    #
    #     main_page.open_friends_list()
    #     friends_page.open_message_dialog()
    #     message_page.delete_message()
    #     message_page.send_message()
    #
    #     auth_page.logout()
    #
    #     auth_page.add_profile()
    #     auth_page.clear_inputs()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)
    #
    #     main_page.open_friends_list()
    #     friends_page.open_message_dialog()
    #
    #     self.assertEqual(message_page.check_message(), dialog.TEST_MESSAGE)
    #
    #     message_page.delete_message()
    #
    #     auth_page.logout()
    #
    #     auth_page.add_profile()
    #     auth_page.clear_inputs()
    #     auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)
    #
    #     main_page.open_friends_list()
    #     friends_page.open_message_dialog()
    #     message_page.delete_message()

    def test_hide_and_show_games_in_feed(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        main_page = MainPage(self.driver)
        main_page.open_games_list()

        games_list = GamesVitrine(self.driver)
        games_list.invite_friend_to_the_game()

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        print('b')
        main_page.open_notification()

        game_page = GamePage(self.driver)
        game_page.block_notifications()

        sleep(3)
