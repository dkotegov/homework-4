from pages.page import Page
from components.settings_game_component import SettingsGameComponent


class SettingsGamePage(Page):
    PAGE = '/settings/feed/apps'

    def __init__(self, driver):
        super(SettingsGamePage, self).__init__(driver)
        self.settings_game_component = SettingsGameComponent(self.driver)

    def delete_from_list(self):
        self.get_hover(self.settings_game_component.get_game_image())
        self.settings_game_component.get_delete_button().click()
        self.settings_game_component.get_confirm_button().click()

