import urlparse

from pages.page import Page
from components.base_settings_component import BaseSettingsForm


class BaseSettingsPage(Page):

    PAGE = 'settings'

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PAGE)
        self.driver.get(url)
        self.driver.maximize_window()

    def personal_data(self):
        baseSettingsForm = BaseSettingsForm(self.driver)
        return baseSettingsForm.personal_data()

    def phone_number(self):
        baseSettingsForm = BaseSettingsForm(self.driver)
        return baseSettingsForm.phone_number()

    def email(self):
        baseSettingsForm = BaseSettingsForm(self.driver)
        return baseSettingsForm.email()

    def profile_get(self):
        baseSettingsForm = BaseSettingsForm(self.driver)
        return baseSettingsForm.profile_get()

    def profile(self):
        baseSettingsForm = BaseSettingsForm(self.driver)
        baseSettingsForm.profile_click()


