from pages.default_page import DefaultPage


class UserSettingsPage(DefaultPage):
    PATH = "user/profile"

    INFO_CHANGE_ERROR = "#settings-error"
    PWD_CHANGE_ERROR = "#settings-password-error"

    NAME = "#settings-name"
    SURNAME = "#settings-surname"
    TELEPHONE = "#settings-phone"
    EMAIL = "#settings-mail"
    DATE = "#settings-birthday"
    SEX = "#settings-gender"

    INFO_SUBMIT = "#settings-button-save"
    INFO_EDIT = "#settings-edit"

    PASSWORD = "#settings-new-pass"
    CONFIRM_PASSWORD = "#settings-confirm-pass"
    OLD_PASSWORD = "#settings-old-pass"

    PASSWORD_SUBMIT = "#settings-save-pass"
    PASSWORD_RESET = "#settings-reset-pass"

    THEME_LIGHT = "#light-theme"
    THEME_DARK = "#dark-theme"

    def input_name_value(self, text):
        self.__input_value__(self.NAME, text)

    def clear_name_value(self):
        self.__clear_input__(self.NAME)

    def is_error_name(self):
        return self.__element_contains_class__(self.NAME, self.ERROR)

    def input_surname_value(self, text):
        self.__input_value__(self.SURNAME, text)

    def clear_surname_value(self):
        self.__clear_input__(self.SURNAME)

    def is_error_surname(self):
        return self.__element_contains_class__(self.SURNAME, self.ERROR)

    def input_telephone_value(self, text):
        self.__input_value__(self.TELEPHONE, text)

    def clear_telephone_value(self):
        self.__clear_input__(self.TELEPHONE)

    def is_error_telephone(self):
        return self.__element_contains_class__(self.TELEPHONE, self.ERROR)

    def input_email_value(self, text):
        self.__input_value__(self.EMAIL, text)

    def clear_email_value(self):
        self.__clear_input__(self.EMAIL)

    def is_error_email(self):
        return self.__element_contains_class__(self.EMAIL, self.ERROR)

    def get_info_change_error(self):
        return self.__get_element__(self.INFO_CHANGE_ERROR).text

    def enter_info_submit(self):
        self.__click_button__(self.INFO_SUBMIT)

    def enter_info_edit(self):
        self.__click_button__(self.INFO_EDIT)

    def input_password_value(self, text):
        self.__input_value__(self.PASSWORD, text)

    def clear_password_value(self):
        self.__clear_input__(self.PASSWORD)

    def is_error_password(self):
        return self.__element_contains_class__(self.PASSWORD, self.ERROR)

    def input_confirm_password_value(self, text):
        self.__input_value__(self.CONFIRM_PASSWORD, text)

    def clear_confirm_password_value(self):
        self.__clear_input__(self.CONFIRM_PASSWORD)

    def is_error_confirm_password(self):
        return self.__element_contains_class__(self.CONFIRM_PASSWORD, self.ERROR)

    def input_old_password_value(self, text):
        self.__input_value__(self.OLD_PASSWORD, text)

    def clear_old_password_value(self):
        self.__clear_input__(self.OLD_PASSWORD)

    def is_error_old_password(self):
        return self.__element_contains_class__(self.OLD_PASSWORD, self.ERROR)

    def get_pwd_change_error(self):
        return self.__get_element__(self.PWD_CHANGE_ERROR).text

    def enter_pwd_submit(self):
        self.__click_button__(self.PASSWORD_SUBMIT)

    def enter_pwd_reset(self):
        self.__click_button__(self.PASSWORD_RESET)

    def get_theme(self):
        html = self.__get_element__("html")

        if self.__contains_class__(html, "theme-light"):
            return "light"

        elif self.__contains_class__(html, "theme-dark"):
            return "dark"

    def change_theme_light(self):
        self.__click_button__(self.THEME_LIGHT)

    def change_theme_dark(self):
        self.__click_button__(self.THEME_DARK)