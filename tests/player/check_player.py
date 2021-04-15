import unittest

from pages.main_page import MainPage
from pages.player_page import PlayerPage
from pages.serial_page import SerialPage
from setup.default_setup import default_setup


class CheckPlayer(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.player_page = PlayerPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.serials_page = SerialPage(self.driver)
        self.main_page.open()

    def test_check_player_appearance(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        self.main_page.move_to_card()
        self.main_page.open_card_player()
        is_all_right = self.main_page.check_player_appearance()
        self.assertTrue(is_all_right)

    def test_check_player_pause_by_pause_btn(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        self.main_page.move_to_card()
        self.main_page.open_card_player()
        self.player_page.set_pause_by_pause_btn()
        is_all_right = self.player_page.check_player_pause()
        self.assertTrue(is_all_right)

    def test_check_player_pause_by_space(self):
        self.main_page.move_to_card()
        self.main_page.open_card_player()
        self.player_page.set_pause_by_space()
        is_all_right = self.player_page.check_player_pause()
        self.assertTrue(is_all_right)

    def test_check_player_pause_by_click(self):
        self.main_page.move_to_card()
        self.main_page.open_card_player()
        self.player_page.set_pause_by_click_on_screen()
        is_all_right = self.player_page.check_player_pause()
        self.assertTrue(is_all_right)

    def test_check_player_mute(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        self.main_page.move_to_card()
        self.main_page.open_card_player()
        is_all_right = self.player_page.check_mute()
        self.assertTrue(is_all_right)

    def test_check_player_sound(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        self.main_page.move_to_card()
        self.main_page.open_card_player()
        is_all_right = self.player_page.check_sound()
        self.assertTrue(is_all_right)

    def test_check_emersion_volume_slider(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        self.main_page.move_to_card()
        self.main_page.open_card_player()
        is_all_right = self.player_page.check_volume_slider()
        self.assertTrue(is_all_right)

    def test_check_share_popup(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        self.main_page.move_to_card()
        self.main_page.open_card_player()
        is_all_right = self.player_page.check_share_popup()
        self.assertTrue(is_all_right)

    def test_check_closing_share_popup(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        self.main_page.move_to_card()
        self.main_page.open_card_player()
        is_all_right = self.player_page.check_closing_share_popup()
        self.assertTrue(is_all_right)

    def test_check_closing_player(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        self.main_page.move_to_card()
        self.main_page.open_card_player()
        is_all_right = self.player_page.check_closing_player()
        self.assertTrue(is_all_right)

    def test_check_switch_next_episode(self):
        self.serials_page.open_auth_popup()
        self.serials_page.auth(self.EMAIL, self.PASSWORD)
        self.serials_page.open()
        self.serials_page.move_to_card()
        self.serials_page.open_card_player()
        is_all_right = self.serials_page.check_switch_next_episode()
        self.assertTrue(is_all_right)

    def test_check_switch_prev_episode(self):
        self.serials_page.open_auth_popup()
        self.serials_page.auth(self.EMAIL, self.PASSWORD)
        self.serials_page.open()
        self.serials_page.move_to_card()
        self.serials_page.open_card_player()
        is_all_right = self.serials_page.check_switch_prev_episode()
        self.assertTrue(is_all_right)

    def tearDown(self):
        self.driver.quit()
