from components.games_list import GamesList
from components.page import Page
from components.settings_out_apps_list import SettingsOutAppsList


class SettingsOutAppsPage(Page):
    PAGE = '/settings/oauth'

    def __init__(self, driver):
        super(SettingsOutAppsPage, self).__init__(driver)
        self.games_list = GamesList(self.driver)

    def delete_app_from_list(self):
        self.get_hover(self.games_list.get_delete_game())
        self.games_list.get_delete_game_button().click()



