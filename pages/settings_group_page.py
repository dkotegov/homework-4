from components.page import Page
from components.settings_group_component import SettingsGroupComponent


class SettingsGroupPage(Page):
    PAGE = '/settings/feed/groups'

    def __init__(self, driver):
        super(SettingsGroupPage, self).__init__(driver)
        self.settings_group_component = SettingsGroupComponent(self.driver)

    def delete_from_list(self):
        self.settings_group_component.get_delete_button().click()
        self.settings_group_component.get_confirm_button().click()
