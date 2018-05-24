from pages.page import Page
from components.settings_man_component import SettingsManComponent


class SettingsManPage(Page):
    PAGE = '/settings/feed/users'

    def __init__(self, driver):
        super(SettingsManPage, self).__init__(driver)
        self.settings_man_component = SettingsManComponent(self.driver)

    def delete_from_list(self):
        self.settings_man_component.get_delete_button().click()
        self.settings_man_component.get_confirm_button().click()