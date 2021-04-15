import unittest

from pages.serial_page import SerialPage
from setup.default_setup import default_setup


class CheckSerialPopup(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.page = SerialPage(self.driver)
        self.page.open()

    def test_seasons_change(self):
        while True:
            self.page.open_popup()
            if self.page.click_season_button():
                break
            else:
                self.page.open()
        is_all_right = self.page.check_season_changed()
        self.assertTrue(is_all_right)

    def test_player_open(self):
        self.page.open_popup()
        self.page.click_serial_episode()
        is_all_right = self.page.check_player_is_open()
        self.assertTrue(is_all_right)

    def tearDown(self):
        self.driver.quit()
