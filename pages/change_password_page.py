from pages.base_page import BasePage


class ChangePasswordPage(BasePage):
    PATH = '/user/{}/password'

    BACK_BTN = 'linkbutton.back-btn'
    CHANGE_BTN = 'input[type="submit"]'

    OLD_PASSWORD_INPUT = 'input[name="oldPassword"]'
    NEW_PASSWORD_INPUT = 'input[name="newPassword"]'
    CONFIRM_PASSWORD_INPUT = 'input[name="confirmPassword"]'

    OLD_PASSWORD_ERROR = '#oldPasswordErrorText'
    NEW_PASSWORD_ERROR = '#newPasswordErrorText'
    CONFIRM_PASSWORD_ERROR = '#confirmPasswordErrorText'

    def __init__(self, driver, username):
        super().__init__(driver, 'div.profile')
        self.PATH = self.PATH.format(username)

    def click_back_btn(self):
        self.locate_el(self.BACK_BTN).click()

    def click_change_btn(self):
        self.locate_el(self.CHANGE_BTN).click()

    def set_old_password(self, password):
        self.set_field(self.OLD_PASSWORD_INPUT, password)

    def set_new_password(self, password):
        self.set_field(self.NEW_PASSWORD_INPUT, password)

    def set_confirm_password(self, password):
        self.set_field(self.CONFIRM_PASSWORD_INPUT, password)

    def get_old_password_error(self):
        return self.locate_el(self.OLD_PASSWORD_ERROR).text

    def get_new_password_error(self):
        return self.locate_el(self.NEW_PASSWORD_ERROR).text

    def get_confirm_password_error(self):
        return self.locate_el(self.CONFIRM_PASSWORD_ERROR).text
