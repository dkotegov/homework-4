from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from helpers import Page, Component
from components import Login, UserSideBar


class UserThemeForm(Component):
    HTML = "html"

    LIGHT = "light"
    DARK = "dark"

    THEME_LIGHT = "#light-theme"
    THEME_DARK = "#dark-theme"

    def get_theme(self):
        html = self.helpers.get_element(self.HTML)

        if self.helpers.is_element_contains_class(html, "theme-light"):
            return self.LIGHT

        elif self.helpers.is_element_contains_class(html, "theme-dark"):
            return self.DARK

    def change_theme_light(self):
        self.helpers.click_element(self.THEME_LIGHT)

    def change_theme_dark(self):
        self.helpers.click_element(self.THEME_DARK)


class UserChangePasswordForm(Component):
    PASSWORD = "#settings-new-pass"
    CONFIRM_PASSWORD = "#settings-confirm-pass"
    OLD_PASSWORD = "#settings-old-pass"

    PASSWORD_SUBMIT = "#settings-save-pass"
    PASSWORD_RESET = "#settings-reset-pass"

    ERROR = "input-error"
    PWD_CHANGE_ERROR = "#settings-password-error"

    def input_password_value(self, text):
        self.helpers.clear_input(self.PASSWORD)
        self.helpers.input_value(self.PASSWORD, text)

    def is_error_password(self):
        return self.helpers.is_contains_class(self.PASSWORD, self.ERROR)

    def input_confirm_password_value(self, text):
        self.helpers.clear_input(self.CONFIRM_PASSWORD)
        self.helpers.input_value(self.CONFIRM_PASSWORD, text)

    def is_error_confirm_password(self):
        return self.helpers.is_contains_class(self.CONFIRM_PASSWORD, self.ERROR)

    def input_old_password_value(self, text):
        self.helpers.clear_input(self.OLD_PASSWORD)
        self.helpers.input_value(self.OLD_PASSWORD, text)

    def is_error_old_password(self):
        return self.helpers.is_contains_class(self.OLD_PASSWORD, self.ERROR)

    def get_pwd_change_error(self):
        return self.helpers.get_element(self.PWD_CHANGE_ERROR).text

    def enter_pwd_submit(self):
        self.helpers.click_element(self.PASSWORD_SUBMIT)

    def enter_pwd_reset(self):
        self.helpers.click_element(self.PASSWORD_RESET)


class UserSettingsForm(Component):
    ERROR = "input-error"

    NAME = "#settings-name"
    SURNAME = "#settings-surname"
    TELEPHONE = "#settings-phone"
    EMAIL = "#settings-email"
    DATE = "#settings-birthday"
    SEX = "#settings-gender"
    SEX_OPTION = "//option[@selected=\"true\"]"
    INFO_SUBMIT = "#settings-button-save"
    INFO_EDIT = "#settings-edit"

    def input_name_value(self, text):
        self.helpers.clear_input(self.NAME)
        self.helpers.input_value(self.NAME, text)

    def is_error_name(self):
        return self.helpers.is_contains_class(self.NAME, self.ERROR)

    def input_surname_value(self, text):
        self.helpers.clear_input(self.SURNAME)
        self.helpers.input_value(self.SURNAME, text)

    def is_error_surname(self):
        return self.helpers.is_contains_class(self.SURNAME, self.ERROR)

    def input_telephone_value(self, text):
        self.helpers.clear_input(self.TELEPHONE)
        self.helpers.input_value(self.TELEPHONE, text)

    def is_error_telephone(self):
        return self.helpers.is_contains_class(self.TELEPHONE, self.ERROR)

    def input_email_value(self, text):
        self.helpers.clear_input(self.EMAIL)
        self.helpers.input_value(self.EMAIL, text)

    def is_error_email(self):
        return self.helpers.is_contains_class(self.EMAIL, self.ERROR)

    def enter_info_submit(self):
        self.helpers.click_element(self.INFO_SUBMIT)

    def enter_info_edit(self):
        self.helpers.click_element(self.INFO_EDIT)

    def input_date_value(self, text):
        self.helpers.clear_input(self.DATE)
        self.helpers.input_value(self.DATE, text)

    def input_sex_value(self, text):
        self.helpers.input_value(self.SEX, text)

    def get_name(self):
        return self.helpers.get_element(self.NAME).get_attribute("value")

    def get_surname(self):
        return self.helpers.get_element(self.SURNAME).get_attribute("value")

    def get_email(self):
        return self.helpers.get_element(self.EMAIL).get_attribute("value")

    def get_sex(self):
        return self.helpers.get_element(self.SEX_OPTION, self.helpers.SELECTOR.XPATH).text


class UserSettingsPage(Page):
    PATH = "/user/profile"

    PAGE = ".settings"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

    @property
    def login(self):
        return Login(self.driver)

    @property
    def side_bar(self):
        return UserSideBar(self.driver)

    @property
    def form(self):
        return UserSettingsForm(self.driver)

    @property
    def pwd_form(self):
        return UserChangePasswordForm(self.driver)

    @property
    def theme_form(self):
        return UserThemeForm(self.driver)
