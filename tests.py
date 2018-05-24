# -*- coding: UTF-8 -*-
import unittest

import os

import time
from selenium.webdriver import DesiredCapabilities, Remote

from components.games_list import GamesList
from components.main_up_toolbar import MainUpToolbar
from components.password_form import PasswordForm
from constants import profiles, dialog, game
from pages.auth_page import AuthPage
# from pages.friends_page import FriendsPage
from pages.black_list_page import BlackList, BlackListPage
from pages.friends_page import FriendsPage
from pages.game_page import GamePage
from pages.games_vitrine import GamesVitrine
from pages.group_page import GroupPage
from pages.main_page import MainPage
from time import sleep

from pages.message_page import MessagePage
from pages.notes_page import NotesPage
from pages.password_page import PasswordPage
from pages.settings_game_page import SettingsGamePage
from pages.settings_group_page import SettingsGroupPage
from pages.settings_man_page import SettingsManPage
from pages.settings_out_apps_page import SettingsOutAppsPage
from pages.settings_page import SettingsPage


class Tests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_add_profile_to_and_delete_from_black_list(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        main_page = MainPage(self.driver)
        main_page.open_friends_list()

        friends_page = FriendsPage(self.driver)
        friends_page.open_message_dialog_with_46()

        message_page = MessagePage(self.driver)
        message_page.open_info_bar()
        message_page.add_to_black_list()
        message_page.accept_to_adding_to_black_list()

        auth_page.logout()

        auth_page.add_profile()
        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        main_page.open_friends_list()
        friends_page.open_message_dialog_with_55()
        message_page.send_message()

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        main_page.open_friends_list()
        friends_page.open_message_dialog_with_46()

        self.assertFalse(message_page.check_message(), False)

        # delete
        black_list = BlackListPage(self.driver)
        black_list.open()
        black_list.delete_from()

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        main_page.open_friends_list()
        friends_page.open_message_dialog_with_55()
        message_page.delete_message()
        message_page.send_message()

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        main_page.open_friends_list()
        friends_page.open_message_dialog_with_46()

        self.assertEqual(message_page.check_message(), dialog.TEST_MESSAGE)

        message_page.delete_message()

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        main_page.open_friends_list()
        friends_page.open_message_dialog_with_55()
        message_page.delete_message()

    def test_hide_and_show_games_in_feed(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        main_page = MainPage(self.driver)
        main_page.open_games_list()

        games_vitrine = GamesVitrine(self.driver)
        games_vitrine.invite_friend_to_the_game()

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        main_page.open_notification()
        main_page.update()
        main_page.open_notification()
        notification_game = main_page.check_notification()

        self.assertTrue(notification_game,
                        games_vitrine.games_list.el)  # Did sender's and receiver's notifications are coincide?

        main_page.hide_notification()
        main_page.update()
        main_page.open_notification()
        checker = main_page.check_notification()

        self.assertFalse(checker, False)  # hide notification

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        main_page.open_games_list()

        self.assertFalse(games_vitrine.invite_friend_to_the_game(), False)  # block to send notification

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        # delete
        settings_game_page = SettingsGamePage(self.driver)
        settings_game_page.open()
        settings_game_page.delete_from_list()

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        main_page.open_games_list()

        self.assertTrue(games_vitrine.invite_friend_to_the_game(), True)

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        main_page.open_notification()

        self.assertTrue(notification_game,
                        games_vitrine.games_list.el)

    def test_current_fake_password_and_new_are_the_same(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        settings_page = SettingsPage(self.driver)
        settings_page.open()
        settings_page.open_password_form()

        password_page = PasswordPage(self.driver)
        password_form = PasswordForm(self.driver)
        password_page.type_fake_current_password()
        password_page.type_new_password()
        password_page.type_retype_password()

        self.assertFalse(password_form.get_password_element(), False)
        self.assertFalse(password_form.get_second_password_element(), False)
        self.assertFalse(password_form.get_third__password_element(), False)

        password_page.submit()

        self.assertTrue(password_form.get_password_element(), True)
        self.assertFalse(password_form.get_second_password_element(), False)
        self.assertFalse(password_form.get_third__password_element(), False)

    def test_current_password_and_new_are_fake_the_same(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        settings_page = SettingsPage(self.driver)
        settings_page.open()
        settings_page.open_password_form()

        password_page = PasswordPage(self.driver)
        password_form = PasswordForm(self.driver)
        password_page.type_current_password()
        password_page.type_new_password()
        password_page.type_fake_retype_password()

        self.assertFalse(password_form.get_password_element(), False)
        self.assertFalse(password_form.get_second_password_element(), False)
        self.assertFalse(password_form.get_third__password_element(), False)

        password_page.submit()

        self.assertFalse(password_form.get_password_element(), False)
        self.assertFalse(password_form.get_second_password_element(), False)
        self.assertTrue(password_form.get_third__password_element(), True)

    def test_unallowed_symbols_in_password(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        settings_page = SettingsPage(self.driver)
        settings_page.open()
        settings_page.open_password_form()

        password_page = PasswordPage(self.driver)
        password_form = PasswordForm(self.driver)
        password_page.type_current_password()
        password_page.type_unallowed_new_password()
        password_page.type_unallowed_retype_password()

        self.assertFalse(password_form.get_password_element(), False)
        self.assertFalse(password_form.get_second_password_element(), False)
        self.assertFalse(password_form.get_third__password_element(), False)

        password_page.submit()

        self.assertFalse(password_form.get_password_element(), False)
        self.assertTrue(password_form.get_second_password_element(), True)
        self.assertFalse(password_form.get_third__password_element(), False)

    def test_hide_groups_from_news(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        group_page = GroupPage(self.driver)
        group_page.open()
        group_page.public_post()
        sending_href = group_page.get_href_from_sender_message()

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        main_page = MainPage(self.driver)
        main_page.go_to_group_news()

        receiver_href = group_page.get_href_from_receiver_message()

        self.assertEqual(receiver_href, sending_href)

        group_page.open()
        group_page.block_page()

        main_page.update()
        main_page.go_to_group_news()

        receiver_href_second = group_page.get_href_from_receiver_message()

        self.assertFalse(receiver_href_second, False)

        settings_group_component = SettingsGroupPage(self.driver)
        settings_group_component.open()
        settings_group_component.delete_from_list()

        main_page.update()
        main_page.go_to_group_news()

        receiver_href_third = group_page.get_href_from_receiver_message()

        self.assertEqual(receiver_href_third, sending_href)

        auth_page.logout()

        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        group_page.open()
        group_page.delete_post()

    def test_hide_man_from_news(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        notes_page = NotesPage(self.driver)
        notes_page.open()
        notes_page.public_note()

        note_sender_href = notes_page.get_href_data()

        auth_page.logout()
        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        main_page = MainPage(self.driver)

        notes_page.open_friends_list()

        note_receiver_href = notes_page.get_receiver_href_data()

        self.assertEqual(note_sender_href, note_receiver_href)

        main_page.open_page_by_url(profiles.PAGE_TECHNOPARK55)
        main_page.block_page()
        main_page.update()

        self.assertFalse(notes_page.get_check_searching(), False)

        settings_man_page = SettingsManPage(self.driver)
        settings_man_page.open()
        settings_man_page.delete_from_list()

        auth_page.logout()
        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK55, profiles.PROFILE_PASSWORD)

        notes_page.open()
        notes_page.delete_note()
        notes_page.public_note()

        note_sender_href_second = notes_page.get_href_data()

        auth_page.logout()
        auth_page.add_profile()
        auth_page.clear_inputs()
        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        notes_page.open_friends_list()

        note_receiver_href_second = notes_page.get_receiver_href_data()

        self.assertEqual(note_sender_href_second, note_receiver_href_second)

    def test_add_and_delete_the_game(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        games_vitrine = GamesVitrine(self.driver)
        games_list = GamesList(self.driver)
        main_page = MainPage(self.driver)
        main_page.open_games_list()
        games_vitrine.participate_to_game()
        #games_vitrine.open_page_by_url(game.THRONEWARS_GAME_URL)
        games_vitrine.check_invite_button()

        main_page = MainPage(self.driver)
        main_page.update()
        main_page.open_games_list()

        self.assertTrue(games_list.get_blood(), True)

        settings_out_apps_page = SettingsOutAppsPage(self.driver)
        settings_out_apps_page.open()
        settings_out_apps_page.delete_app_from_list()

        games_vitrine.open()

        self.assertFalse(games_vitrine.open(), False)
