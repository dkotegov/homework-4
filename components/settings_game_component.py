from components.base_component import BaseComponent


class SettingsGameComponent(BaseComponent):
    IMAGE = "//a[contains(@href, '/thronewars')]"
    DELETE_BUTTON = "//a[contains(@class, 'gwt-shortcutMenu-iconlink-item')]"
    CONFIRM_BUTTON = "//input[@data-l='t,confirm']"

    def get_game_image(self):
        return self.get_clickable_element(self.IMAGE)

    def get_delete_button(self):
        return self.get_clickable_element(self.DELETE_BUTTON)

    def get_confirm_button(self):
        return self.get_clickable_element(self.CONFIRM_BUTTON)
