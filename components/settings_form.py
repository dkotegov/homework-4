from components.base_component import BaseComponent


class SettingsForm(BaseComponent):
    SETTINGS_FORM = "//a[contains(@href, 'ChangePassword')]"
    CHANGE_PASSWORD_BUTTON = "//div[contains(@class,'user-settings_i_lk lstp-t al')]"

    def get_settings_form_button(self):
        return self.driver.find_elements_by_xpath(self.CHANGE_PASSWORD_BUTTON)[1]

    def get_settings_hover_element(self):
        return self.get_clickable_element(self.SETTINGS_FORM)
