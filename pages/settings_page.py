from pages.page import Page
from components.settings_form import SettingsForm


class SettingsPage(Page):
    PAGE = '/settings'

    def __init__(self, driver):
        super(SettingsPage, self).__init__(driver)
        self.settings_form = SettingsForm(self.driver)

    def open_password_form(self):
        self.get_hover(self.settings_form.get_settings_hover_element())
        self.settings_form.get_settings_form_button().click()

