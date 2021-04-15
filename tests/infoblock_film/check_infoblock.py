import unittest

from pages.serial_page import SerialPage
from setup.default_setup import default_setup


class CheckInfoblock(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.page = SerialPage(self.driver)
        self.page.open()

    def test_details_block_click(self):
        self.page.open_infoblock()
        self.page.click_infoblock_details()
        is_all_right = self.page.check_infoblock_details_open()
        self.assertTrue(is_all_right)

    def test_seasons_block_click(self):
        self.page.open_infoblock()
        self.page.click_infoblock_seasons()
        is_all_right = self.page.check_infoblock_seasons_open()
        self.assertTrue(is_all_right)

    def test_season_click(self):
        self.page.open_infoblock()
        self.page.click_infoblock_seasons()
        is_infoblock_open = self.page.check_infoblock_seasons_open()
        self.assertTrue(is_infoblock_open)
        self.page.click_infoblock_season_button()
        is_all_right = self.page.check_episodes_open()
        self.assertTrue(is_all_right)

    def test_player_open(self):
        self.page.open_infoblock()
        self.page.click_infoblock_seasons()
        is_infoblock_open = self.page.check_infoblock_seasons_open()
        self.assertTrue(is_infoblock_open)
        self.page.click_episode()
        is_all_right = self.page.check_player_open()
        self.assertTrue(is_all_right)

    def test_infoblock_close(self):
        self.page.open_infoblock()
        self.page.close_infoblock()
        is_all_right = self.page.check_infoblock_close()
        self.assertTrue(is_all_right)

    def tearDown(self):
        self.driver.quit()
