from pages.page import Page
from components.password_form import PasswordForm
from constants import profiles


class PasswordPage(Page):

    def __init__(self, driver):
        super(PasswordPage, self).__init__(driver)
        self.password_form = PasswordForm(self.driver)

    def type_current_password(self):
        self.password_form.get_current_password_input().send_keys(profiles.PROFILE_PASSWORD)

    def type_fake_current_password(self):
        self.password_form.get_current_password_input().send_keys(profiles.FAKE_CURRENT_PASSWORD)

    def type_retype_password(self):
        self.password_form.get_retype_password_input().send_keys(profiles.NEW_PASSWORD)

    def type_fake_retype_password(self):
        self.password_form.get_retype_password_input().send_keys(profiles.FAKE_RETYPE_PASSWORD)

    def type_new_password(self):
        self.password_form.get_new_password_input().send_keys(profiles.NEW_PASSWORD)

    def type_fake_new_password(self):
        self.password_form.get_new_password_input().send_keys(profiles.FAKE_RETYPE_PASSWORD)

    def type_unallowed_new_password(self):
        self.password_form.get_new_password_input().send_keys(profiles.UNALLOWED_PASSWORD)

    def type_unallowed_retype_password(self):
        self.password_form.get_retype_password_input().send_keys(profiles.UNALLOWED_PASSWORD)

    def submit(self):
        self.password_form.get_submit().click()

    # def change_to_ancient_data(self):
