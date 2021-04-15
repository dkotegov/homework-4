from pages.base import BasePage
from components.player import Player


class PlayerPage(BasePage):
    """
    Главная Страница
    """

    def __init__(self, driver):
        self.PATH = 'watch/'
        super(PlayerPage, self).__init__(driver, '')
        self.player = Player(self.driver)

    def set_pause_by_pause_btn(self):
        self.player.move_to_player_bar()
        self.player.click_on_btn_pause()

    def set_pause_by_space(self):
        self.player.click_on_space()

    def set_pause_by_click_on_screen(self):
        self.player.click_on_screen()

    def check_mute(self) -> bool:
        self.player.move_to_player_bar()
        self.player.click_on_sound()
        return self.player.check_mute()

    def check_sound(self) -> bool:
        self.player.move_to_player_bar()
        self.player.click_on_sound()
        self.player.click_on_mute()
        return self.player.check_sound()

    def check_volume_slider(self) -> bool:
        self.player.move_to_player_bar()
        self.player.move_to_volume_btn()
        return self.player.check_volume_slider()

    def check_share_popup(self) -> bool:
        self.player.move_to_player_bar()
        self.player.click_on_share_btn()
        return self.player.check_share_popup()

    def check_closing_share_popup(self) -> bool:
        self.player.move_to_player_bar()
        self.player.click_on_share_btn()
        self.player.click_on_close_share_popup()
        return self.player.check_disappear_share_popup()

    def check_closing_player(self) -> bool:
        self.player.click_on_close_player_btn()
        return self.player.check_disappear_player()

    def check_player_pause(self) -> bool:
        return self.player.check_paused()
