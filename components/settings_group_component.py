from components.base_component import BaseComponent


class SettingsGroupComponent(BaseComponent):
    DELETE_BUTTON = "//div[contains(@class, 'ic12 ic12_close-w')]"
    CONFIRM_BUTTON = "//input[@data-l='t,confirm']"

    def get_delete_button(self):
        return self.get_clickable_element(self.DELETE_BUTTON)

    def get_confirm_button(self):
        return self.get_visibility_element(self.CONFIRM_BUTTON)