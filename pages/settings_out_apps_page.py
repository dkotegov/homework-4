from components.page import Page
from components.settings_out_apps_list import SettingsOutAppsList


class SettingsOutAppsPage(Page):
    PAGE = '/settings/oauth'

    def delete_app_from_list(self):
        settings_out_apps_list = SettingsOutAppsList(self.driver)
