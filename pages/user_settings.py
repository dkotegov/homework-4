from helpers import Page, Component
from components import Login, SideBar


class UserThemeForm(Component):
    THEME_LIGHT = "#light-theme"
    THEME_DARK = "#dark-theme"

    def get_theme(self):
        html = self.helpers.get_element("html")

        if self.helpers.is_element_contains_class(html, "theme-light"):
            return "light"

        elif self.helpers.is_element_contains_class(html, "theme-dark"):
            return "dark"

    def change_theme_light(self):
        self.helpers.click_button(self.THEME_LIGHT)

    def change_theme_dark(self):
        self.helpers.click_button(self.THEME_DARK)


class UserChangePasswordForm(Component):
    PASSWORD = "#settings-new-pass"
    CONFIRM_PASSWORD = "#settings-confirm-pass"
    OLD_PASSWORD = "#settings-old-pass"

    PASSWORD_SUBMIT = "#settings-save-pass"
    PASSWORD_RESET = "#settings-reset-pass"

    ERROR = "input-error"
    PWD_CHANGE_ERROR = "#settings-password-error"

    def input_password_value(self, text):
        self.helpers.input_value(self.PASSWORD, text)

    def clear_password_value(self):
        self.helpers.clear_input(self.PASSWORD)

    def is_error_password(self):
        return self.helpers.is_contains_class(self.PASSWORD, self.ERROR)

    def input_confirm_password_value(self, text):
        self.helpers.input_value(self.CONFIRM_PASSWORD, text)

    def clear_confirm_password_value(self):
        self.helpers.clear_input(self.CONFIRM_PASSWORD)

    def is_error_confirm_password(self):
        return self.helpers.is_contains_class(self.CONFIRM_PASSWORD, self.ERROR)

    def input_old_password_value(self, text):
        self.helpers.input_value(self.OLD_PASSWORD, text)

    def clear_old_password_value(self):
        self.helpers.clear_input(self.OLD_PASSWORD)

    def is_error_old_password(self):
        return self.helpers.is_contains_class(self.OLD_PASSWORD, self.ERROR)

    def get_pwd_change_error(self):
        return self.helpers.get_element(self.PWD_CHANGE_ERROR).text

    def enter_pwd_submit(self):
        self.helpers.click_button(self.PASSWORD_SUBMIT)

    def enter_pwd_reset(self):
        self.helpers.click_button(self.PASSWORD_RESET)


class UserSettingsForm(Component):
    ERROR = "input-error"

    INFO_CHANGE_ERROR = "#settings-error"

    NAME = "#settings-name"
    SURNAME = "#settings-surname"
    TELEPHONE = "#settings-phone"
    EMAIL = "#settings-email"
    DATE = "#settings-birthday"
    SEX = "#settings-gender"

    INFO_SUBMIT = "#settings-button-save"
    INFO_EDIT = "#settings-edit"

    def input_name_value(self, text):
        self.helpers.input_value(self.NAME, text)

    def clear_name_value(self):
        self.helpers.clear_input(self.NAME)

    def is_error_name(self):
        return self.helpers.is_contains_class(self.NAME, self.ERROR)

    def input_surname_value(self, text):
        self.helpers.input_value(self.SURNAME, text)

    def clear_surname_value(self):
        self.helpers.clear_input(self.SURNAME)

    def is_error_surname(self):
        return self.helpers.is_contains_class(self.SURNAME, self.ERROR)

    def input_telephone_value(self, text):
        self.helpers.input_value(self.TELEPHONE, text)

    def clear_telephone_value(self):
        self.helpers.clear_input(self.TELEPHONE)

    def is_error_telephone(self):
        return self.helpers.is_contains_class(self.TELEPHONE, self.ERROR)

    def input_email_value(self, text):
        self.helpers.input_value(self.EMAIL, text)

    def clear_email_value(self):
        self.helpers.clear_input(self.EMAIL)

    def is_error_email(self):
        return self.helpers.is_contains_class(self.EMAIL, self.ERROR)

    def get_info_change_error(self):
        return self.helpers.get_element(self.INFO_CHANGE_ERROR).text

    def enter_info_submit(self):
        self.helpers.click_button(self.INFO_SUBMIT)

    def enter_info_edit(self):
        self.helpers.click_button(self.INFO_EDIT)
        
        
class UserSettingsPage(Page):
    PATH = "user/profile"

    @property
    def login(self):
        return Login(self.driver)

    @property
    def side_bar(self):
        return SideBar(self.driver)

    @property
    def form(self):
        return UserSettingsForm(self.driver)

    @property
    def pwd_form(self):
        return UserChangePasswordForm(self.driver)

    @property
    def theme_form(self):
        return UserThemeForm(self.driver)