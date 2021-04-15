import unittest

from pages.main_page import MainPage
from setup.default_setup import default_setup


class CheckMain(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.page = MainPage(self.driver)
        self.page.open()
    
    def test_check_preview_player_appearance(self):
        self.page.open_auth_popup()
        self.page.auth(self.EMAIL, self.PASSWORD)
        self.page.open_player()
        is_all_right = self.page.check_player_appearance()
        self.assertTrue(is_all_right)

    def test_check_preview_info_popup_appearance(self):
        self.page.open_preview_info_popup()
        is_all_right = self.page.check_info_popup_appearance()
        self.assertTrue(is_all_right)

    def test_check_card_info_block_appearance(self):
        self.page.move_to_card()
        self.page.open_card_info_block()
        is_all_right = self.page.check_info_block_appearance()
        self.assertTrue(is_all_right)

    def test_check_card_player_appearance(self):
        self.page.open_auth_popup()
        self.page.auth(self.EMAIL, self.PASSWORD)
        self.page.move_to_card()
        self.page.open_card_player()
        is_all_right = self.page.check_player_appearance()
        self.assertTrue(is_all_right)

    def test_check_card_info_block_appearance_via_card_click(self):
        self.page.open_card_info_block_via_card_click()
        is_all_right = self.page.check_info_block_appearance()
        self.assertTrue(is_all_right)

    def test_check_like_needs_auth(self):
        self.page.open_infoblock()
        self.page.click_like()
        is_all_right = self.page.check_auth_popup_open()
        self.assertTrue(is_all_right)

    def test_check_dislike_needs_auth(self):
        self.page.open_infoblock()
        self.page.click_dislike()
        is_all_right = self.page.check_auth_popup_open()
        self.assertTrue(is_all_right)

    def test_check_add_my_list_needs_auth(self):
        self.page.open_infoblock()
        self.page.click_add_my_list_infoblock()
        is_all_right = self.page.check_auth_popup_open()
        self.assertTrue(is_all_right)

    def test_check_add_my_list_button(self):
        self.page.open_auth_popup()
        self.page.auth(self.EMAIL, self.PASSWORD)
        is_auth_right = self.page.check_auth()
        self.assertTrue(is_auth_right)
        self.page.open_popup()
        self.page.click_add_my_list_popup()
        is_all_right = self.page.check_add_my_list_clicked()
        self.assertTrue(is_all_right)

    def tearDown(self):
        self.driver.quit()
